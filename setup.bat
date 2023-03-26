@echo off

where poetry
if %ERRORLEVEL% NEQ 0 python utils/install_poetry.py
set PATH=%PATH%;%USERPROFILE%\AppData\Roaming\pypoetry\venv\Scripts

rem install dependencies
poetry install
poetry shell
