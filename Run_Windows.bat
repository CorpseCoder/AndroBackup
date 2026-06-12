cd /d %~dp0

python setup.py

call env\Scripts\activate.bat

python main.py

deactivate
