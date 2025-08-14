installation

```
git clone https://github.com/Rosellines/GenerateBarcodetoko
cd GenerateBarcodetoko
```
```
python -m pip install pillow python-barcode
python.exe -m pip install pillow python-barcode
python.exe -m pip install pandas openpyxl
pip install pandas
```
then, make environment
```
python -m venv barcode
source barcode/bin/activate
```
then, run it.
1. Run generate label.py if u want to create single barcode
2. Run generate by excel if u want to bulk barcode
```
python3 generate_label.py
```
```
python3 generate_by_excel.py
```
