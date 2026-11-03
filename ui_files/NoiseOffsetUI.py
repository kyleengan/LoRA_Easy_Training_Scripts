# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NoiseOffsetUI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)

from modules.LineEditHighlight import LineEditWithHighlight
from modules.ScrollOnSelect import (DoubleSpinBox, SpinBox)

class Ui_noise_offset_UI(object):
    def setupUi(self, noise_offset_UI):
        if not noise_offset_UI.objectName():
            noise_offset_UI.setObjectName(u"noise_offset_UI")
        noise_offset_UI.resize(400, 140)
        self.formLayout_2 = QFormLayout(noise_offset_UI)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.noise_offset_enable = QCheckBox(noise_offset_UI)
        self.noise_offset_enable.setObjectName(u"noise_offset_enable")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.noise_offset_enable)

        self.noise_offset_input = LineEditWithHighlight(noise_offset_UI)
        self.noise_offset_input.setObjectName(u"noise_offset_input")
        self.noise_offset_input.setEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.noise_offset_input)

        self.pyramid_noise_enable = QCheckBox(noise_offset_UI)
        self.pyramid_noise_enable.setObjectName(u"pyramid_noise_enable")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.pyramid_noise_enable)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(noise_offset_UI)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.pyramid_iteration_input = SpinBox(noise_offset_UI)
        self.pyramid_iteration_input.setObjectName(u"pyramid_iteration_input")
        self.pyramid_iteration_input.setEnabled(False)
        self.pyramid_iteration_input.setFocusPolicy(Qt.StrongFocus)
        self.pyramid_iteration_input.setMinimum(1)
        self.pyramid_iteration_input.setValue(6)

        self.horizontalLayout.addWidget(self.pyramid_iteration_input)

        self.label_3 = QLabel(noise_offset_UI)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.pyramid_discount_input = DoubleSpinBox(noise_offset_UI)
        self.pyramid_discount_input.setObjectName(u"pyramid_discount_input")
        self.pyramid_discount_input.setEnabled(False)
        self.pyramid_discount_input.setFocusPolicy(Qt.StrongFocus)
        self.pyramid_discount_input.setMinimum(0.010000000000000)
        self.pyramid_discount_input.setSingleStep(0.010000000000000)
        self.pyramid_discount_input.setValue(0.300000000000000)

        self.horizontalLayout.addWidget(self.pyramid_discount_input)


        self.formLayout_2.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)

        self.immiscible_enable = QCheckBox(noise_offset_UI)
        self.immiscible_enable.setObjectName(u"immiscible_enable")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.immiscible_enable)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(noise_offset_UI)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.immiscible_k_input = SpinBox(noise_offset_UI)
        self.immiscible_k_input.setObjectName(u"immiscible_k_input")
        self.immiscible_k_input.setEnabled(False)
        self.immiscible_k_input.setFocusPolicy(Qt.StrongFocus)
        self.immiscible_k_input.setMinimum(2)
        self.immiscible_k_input.setMaximum(64)
        self.immiscible_k_input.setValue(8)

        self.horizontalLayout_2.addWidget(self.immiscible_k_input)


        self.formLayout_2.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)

        self.dream_enable = QCheckBox(noise_offset_UI)
        self.dream_enable.setObjectName(u"dream_enable")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.dream_enable)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(noise_offset_UI)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.dream_p_input = DoubleSpinBox(noise_offset_UI)
        self.dream_p_input.setObjectName(u"dream_p_input")
        self.dream_p_input.setEnabled(False)
        self.dream_p_input.setFocusPolicy(Qt.StrongFocus)
        self.dream_p_input.setMinimum(0.050000000000000)
        self.dream_p_input.setMaximum(5.000000000000000)
        self.dream_p_input.setSingleStep(0.100000000000000)
        self.dream_p_input.setValue(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.dream_p_input)


        self.formLayout_2.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_3)


        self.retranslateUi(noise_offset_UI)

        QMetaObject.connectSlotsByName(noise_offset_UI)
    # setupUi

    def retranslateUi(self, noise_offset_UI):
        noise_offset_UI.setWindowTitle(QCoreApplication.translate("noise_offset_UI", u"Form", None))
#if QT_CONFIG(tooltip)
        noise_offset_UI.setToolTip(QCoreApplication.translate("noise_offset_UI", u"<html><head/><body><p>Noise Offset is a tweak to the noise of models, Typically EDM based models like 1.X and SDXL, that allows for a larger range of color</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.noise_offset_enable.setText(QCoreApplication.translate("noise_offset_UI", u"Noise Offset", None))
#if QT_CONFIG(tooltip)
        self.noise_offset_input.setToolTip(QCoreApplication.translate("noise_offset_UI", u"<html><head/><body><p>Noise Offset is a tweak to the noise of models, Typically EDM based models like 1.X and SDXL, that allows for a larger range of color</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.noise_offset_input.setText(QCoreApplication.translate("noise_offset_UI", u"0.1", None))
#if QT_CONFIG(tooltip)
        self.pyramid_noise_enable.setToolTip(QCoreApplication.translate("noise_offset_UI", u"<html><head/><body><p>Pyramid Noise, otherwise known as Multires Noise is a tweak to the noise, much like Noise Offset, but is less destructive.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pyramid_noise_enable.setText(QCoreApplication.translate("noise_offset_UI", u"Pyramid Noise", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("noise_offset_UI", u"<html><head/><body><p>Pyramid Noise, otherwise known as Multires Noise is a tweak to the noise, much like Noise Offset, but is less destructive.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("noise_offset_UI", u"Iterations", None))
#if QT_CONFIG(tooltip)
        self.pyramid_iteration_input.setToolTip(QCoreApplication.translate("noise_offset_UI", u"<html><head/><body><p>Pyramid Noise, otherwise known as Multires Noise is a tweak to the noise, much like Noise Offset, but is less destructive.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("noise_offset_UI", u"<html><head/><body><p>Pyramid Noise, otherwise known as Multires Noise is a tweak to the noise, much like Noise Offset, but is less destructive.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("noise_offset_UI", u"Discount", None))
#if QT_CONFIG(tooltip)
        self.pyramid_discount_input.setToolTip(QCoreApplication.translate("noise_offset_UI", u"<html><head/><body><p>Pyramid Noise, otherwise known as Multires Noise is a tweak to the noise, much like Noise Offset, but is less destructive.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.immiscible_enable.setToolTip(QCoreApplication.translate("noise_offset_UI", u"<html><head/><body><p>Immiscible noise pairing (KNN): for each image, k noise samples are drawn and the one closest to the image latent is used. Reported to speed up convergence. Works at any batch size. Not used by Flux.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.immiscible_enable.setText(QCoreApplication.translate("noise_offset_UI", u"Immiscible Noise", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("noise_offset_UI", u"<html><head/><body><p>Number of noise candidates per image (k). Around 4-8 is a reasonable start; larger values pair more strongly.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("noise_offset_UI", u"Candidates (k)", None))
#if QT_CONFIG(tooltip)
        self.immiscible_k_input.setToolTip(QCoreApplication.translate("noise_offset_UI", u"<html><head/><body><p>Number of noise candidates per image (k). Around 4-8 is a reasonable start; larger values pair more strongly.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dream_enable.setToolTip(QCoreApplication.translate("noise_offset_UI", u"<html><head/><body><p>DREAM (experimental): adds one extra no-grad forward pass per step and trains on inputs rectified with the model's own prediction, reducing exposure bias. Roughly +25-35% time per step. Gains are proven only for super-resolution; A/B test it. SD 1.5 / SDXL LoRA only (not Flux or Textual Inversion).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dream_enable.setText(QCoreApplication.translate("noise_offset_UI", u"DREAM (experimental)", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("noise_offset_UI", u"<html><head/><body><p>Detail preservation exponent p in lambda = sqrt(1 - alpha_bar)^p. 1.0 is the paper's best; values near 0 apply full strength at every timestep, larger values weaken the effect at low noise levels.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("noise_offset_UI", u"Detail Preservation (p)", None))
#if QT_CONFIG(tooltip)
        self.dream_p_input.setToolTip(QCoreApplication.translate("noise_offset_UI", u"<html><head/><body><p>Detail preservation exponent p in lambda = sqrt(1 - alpha_bar)^p. 1.0 is the paper's best; values near 0 apply full strength at every timestep, larger values weaken the effect at low noise levels.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

