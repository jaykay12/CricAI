Welcome to the **CricAI** desktop application! 🏏

---

## 🛠 Requirements

* **Python 3.x**
* **PyQt5**
* **Qt Designer**

---

## 🚀 Building the Project

Follow these steps to set up the development environment and get the application running:

1. Clone the project using `git clone https://github.com/jaykay12/CricAI.git`
2. Explore into the Desktop-App sections using `cd CricAI`
3. Create a Virtual Env using `python3 -m virtualenv venv`
4. Activate the Virtual Env using `source venv/bin/activate`
5. Install all dependencies using `pip install -r requirements.txt`


## 🎨 Installing Qt Designer
Use the following commands based on your operating system:

### Linux (Ubuntu/Debian)

`sudo apt-get install qt-designer`

### macOS

`brew install qt@5`

## ⚙️ Running the Classifier Models

Follow these steps to generate the UI components, prepare the models, and launch the application:

1. Navigate to the desktop application directory using `cd src/desktop`
2. Load any UI file into QT Designer using `designer CricAI_Basic.ui`
3. Convert UI code to Python code using `pyuic5 -x CricAI_Basic.ui -o CricAI_Basic.py`
4. Pickle your classifiers using `python3 ../core/modelPickler.py`
5. Run the App using `python3 main.py`


**Extra Information:**
 - Convert UI Image file to Python Image File using `pyrcc5 projectImage.qrc -o projectImage_rc.py`
