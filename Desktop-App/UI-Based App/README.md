## *Requirements for the project*
 - PyQT5
 - QT Designer
 - Python3

## *Building the Project:*
1. Clone the project using `git clone https://github.com/jaykay12/CricAI.git`
2. Explore into the Desktop-App sections using `cd CricAI/Desktop-App`
3. Create a Virtual Env using `virtualenv venv`
4. Activate the Virtual Env using `cd venv/bin` & then, `source activate`
5. Install all dependencies using `pip install -r requirements.txt`
6. Install QT Designer on your workspace using `sudo apt-get install qt-designer`

## *Running the Classifier Models:*
1. Change directory to the UI-Based Desktop App using `cd UI-Based App`
2. Load any UI file from QT Designer using `designer CricAI_Basic.ui`
3. Convert UI code to Python code using `pyuic5 -x CricAI_Basic.ui -o CricAI_Basic.py`
4. Pickle your classifiers using `python3 modelPickler.py`
5. Run the App using `python3 main.py`


**Extra Information:**
 - Convert UI Image file to Python Image File using `pyrcc5 projectImage.qrc -o projectImage_rc.py`
