*Requirements*

 - PyQT5
 - QT Designer
 - Python3

*Running the Project:*

1. Load any UI file from QT Designer using `designer CricAI_Basic.ui`
2. Convert UI code to Python code using `pyuic5 -x CricAI_Basic.ui -o CricAI_Basic.py`
3. Pickle your classifiers using `python3 modelPickler.py`
4. Run the App using `python3 main.py`

*Extra Information:*

 - Convert UI Image file to Python Image File using `pyrcc5 projectImage.qrc -o projectImage_rc.py`