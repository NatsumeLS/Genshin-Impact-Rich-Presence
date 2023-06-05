py -m pip install --upgrade pip
If Not Exist "venv\Scripts\activate.bat" (
    py -m venv venv
)
venv\Scripts\activate.bat &^
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu118 &^
py -m pip install -r requirements.txt &^
py main.py