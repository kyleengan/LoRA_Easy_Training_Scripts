@echo off

title LoRA Trainer
cd %~dp0
call venv\Scripts\activate
py main.py
pause
