from PySide6.QtWidgets import QWidget
from ui_files.NoiseOffsetUI import Ui_noise_offset_UI
from modules.BaseWidget import BaseWidget


class NoiseOffsetWidget(BaseWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.colap.set_title("Noise Args")
        self.widget = Ui_noise_offset_UI()

        self.name = "noise_args"

        # DREAM / immiscible support depends on the training target, tracked from outside
        self.is_flux = False
        self.is_ti = False

        self.setup_widget()
        self.setup_connections()

    def setup_widget(self) -> None:
        super().setup_widget()
        self.widget.setupUi(self.content)

    def setup_connections(self) -> None:
        self.widget.noise_offset_enable.clicked.connect(
            self.enable_disable_noise_offset
        )
        self.widget.noise_offset_input.textChanged.connect(
            lambda x: self.edit_args("noise_offset", x, True)
        )
        self.widget.pyramid_noise_enable.clicked.connect(
            self.enable_disable_pyramid_noise
        )
        self.widget.pyramid_iteration_input.valueChanged.connect(
            lambda x: self.edit_args("multires_noise_iterations", x, True)
        )
        self.widget.pyramid_discount_input.valueChanged.connect(
            lambda x: self.edit_args("multires_noise_discount", round(x, 4), True)
        )
        self.widget.immiscible_enable.clicked.connect(self.enable_disable_immiscible)
        self.widget.immiscible_k_input.valueChanged.connect(
            lambda x: self.edit_args("immiscible_noise_k", x, True)
        )
        self.widget.dream_enable.clicked.connect(self.enable_disable_dream)
        # p may legitimately be 0.0, so it is not "optional" (optional args drop falsy values)
        self.widget.dream_p_input.valueChanged.connect(
            lambda x: self.edit_args("dream_detail_preservation", round(x, 4))
        )

    def edit_args(self, name: str, value: object, optional: bool = False) -> None:
        if isinstance(value, str):
            try:
                value = float(value)
            except ValueError:
                return super().edit_args(name, 0, optional)
        return super().edit_args(name, value, optional)

    def enable_disable_noise_offset(self, toggle: bool) -> None:
        if "noise_offset" in self.args:
            del self.args["noise_offset"]
        self.widget.noise_offset_input.setEnabled(toggle)
        if not toggle:
            return
        self.edit_args("noise_offset", self.widget.noise_offset_input.text(), True)

    def enable_disable_pyramid_noise(self, toggle: bool) -> None:
        args = ["multires_noise_iterations", "multires_noise_discount"]
        for arg in args:
            if arg in self.args:
                del self.args[arg]
        self.widget.pyramid_iteration_input.setEnabled(toggle)
        self.widget.pyramid_discount_input.setEnabled(toggle)
        if not toggle:
            return
        self.edit_args(
            "multires_noise_iterations",
            self.widget.pyramid_iteration_input.value(),
            True,
        )
        self.edit_args(
            "multires_noise_discount",
            round(self.widget.pyramid_discount_input.value(), 4),
            True,
        )

    def enable_disable_immiscible(self, toggle: bool) -> None:
        if "immiscible_noise_k" in self.args:
            del self.args["immiscible_noise_k"]
        self.widget.immiscible_k_input.setEnabled(toggle)
        if not toggle:
            return
        self.edit_args("immiscible_noise_k", self.widget.immiscible_k_input.value(), True)

    def enable_disable_dream(self, toggle: bool) -> None:
        for arg in ["dream_training", "dream_detail_preservation"]:
            if arg in self.args:
                del self.args[arg]
        self.widget.dream_p_input.setEnabled(toggle)
        if not toggle:
            return
        self.edit_args("dream_training", True, True)
        self.edit_args("dream_detail_preservation", round(self.widget.dream_p_input.value(), 4))

    # --- external state: which training target is selected ---

    def set_flux(self, is_flux: bool) -> None:
        self.is_flux = is_flux
        self.update_support()

    def set_ti(self, is_ti: bool) -> None:
        self.is_ti = is_ti
        self.update_support()

    def update_support(self) -> None:
        # Flux builds its own noise, so neither feature applies there.
        # DREAM is only wired into the SD1.5 / SDXL LoRA trainer (not textual inversion).
        immiscible_ok = not self.is_flux
        dream_ok = not self.is_flux and not self.is_ti

        self.widget.immiscible_enable.setEnabled(immiscible_ok)
        if not immiscible_ok and self.widget.immiscible_enable.isChecked():
            self.widget.immiscible_enable.setChecked(False)
            self.enable_disable_immiscible(False)

        self.widget.dream_enable.setEnabled(dream_ok)
        if not dream_ok and self.widget.dream_enable.isChecked():
            self.widget.dream_enable.setChecked(False)
            self.enable_disable_dream(False)

    def load_args(self, args: dict) -> bool:
        # the flux widget loads after this one, so read the flux state from the config being loaded
        self.is_flux = bool(args.get("flux_args"))
        args: dict = args.get(self.name, {})

        # update element inputs
        self.widget.noise_offset_enable.setChecked(
            bool(args.get("noise_offset", False))
        )
        self.widget.noise_offset_input.setText(str(args.get("noise_offset", 0.1)))
        self.widget.pyramid_noise_enable.setChecked(
            bool(args.get("multires_noise_iterations", False))
        )
        self.widget.pyramid_iteration_input.setValue(
            args.get("multires_noise_iterations", 6)
        )
        self.widget.pyramid_discount_input.setValue(
            args.get("multires_noise_discount", 0.3)
        )
        self.widget.immiscible_enable.setChecked(
            bool(args.get("immiscible_noise_k", False))
        )
        self.widget.immiscible_k_input.setValue(args.get("immiscible_noise_k", 8))
        self.widget.dream_enable.setChecked(bool(args.get("dream_training", False)))
        self.widget.dream_p_input.setValue(args.get("dream_detail_preservation", 1.0))

        # edit args to match
        self.enable_disable_noise_offset(self.widget.noise_offset_enable.isChecked())
        self.enable_disable_pyramid_noise(self.widget.pyramid_noise_enable.isChecked())
        self.enable_disable_immiscible(self.widget.immiscible_enable.isChecked())
        self.enable_disable_dream(self.widget.dream_enable.isChecked())
        self.update_support()
        return True
