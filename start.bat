@echo off
echo Starting genshin discord rpc
py -m pip install --upgrade pip
If Not Exist "venv\Scripts\activate.bat" (
    py -m venv venv
)
venv\Scripts\activate.bat &^
py install.py &^
py main.py