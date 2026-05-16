# 🏏 CricAI
https://cricai.onrender.com


A machine learning-powered web application for cricket. This repository contains the source code, pre-trained model handlers, and deployment configurations to get the application running locally or in the cloud.

---

## 🛠️ Build & Local Setup

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Environment](https://img.shields.io/badge/Environment-Virtualenv-orange.svg)

Follow these steps to set up your local development environment:

1. **Clone the repository**
    ```bash
    git clone https://github.com/jaykay12/CricAI.git
    ```
2. **Create & Activate the Virtual Environment**
    ```bash
    cd CricAI/Web-App
    python3 -m virtualenv venv
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Running on Local

Once your environment is set up and dependencies are installed, you can boot up the application locally after Serialising the classifiers:

```bash
python3 modelPickler.py
python3 index.py
```


Service boots up @ [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---


## ☁️ Cloud Hosting

![Provider](https://img.shields.io/badge/Provider-Render-blue.svg)
![Deployed](https://img.shields.io/badge/Deployed-Success-brightgreen.svg)


When setting up your web service on Render, simply use the following run command:

```bash
gunicorn index:app
```

---

## Deprecated 

### Hosting on Heroku (Not Free anymore)

![Provider](https://img.shields.io/badge/Provider-Heroku-orange.svg)
![Deployed](https://img.shields.io/badge/Deployed-Down-red.svg)

1. Login to your heroku account on workspace using `heroku login` & then providing credentials.
2. Create the app using `heroku create <*NameOfApp*>` e.g `heroku create cricai`
3. Set Buildpacks for the app using `heroku buildpacks:set heroku/python`
4. Generate a file using `pip freeze > requirements.txt`
5. Create a file named *Procfile* with contents as `web: gunicorn index:app`
6. Commit the steps using `git add .` & then, `git commit -m "MESSAGE"`
7. Push for deploy using `git push heroku master`