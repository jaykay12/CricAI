# 🏏 CricAI
https://cricai.onrender.com

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Environment](https://img.shields.io/badge/Environment-Virtualenv-orange.svg)
![Deployment](https://img.shields.io/badge/Deployment-Render-brightgreen.svg)

A machine learning-powered web application for cricket. This repository contains the source code, pre-trained model handlers, and deployment configurations to get the application running locally or in the cloud.

---

## 🛠️ Build & Local Setup

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

## 🚀 Running on Local

Once your environment is set up and dependencies are installed, you can boot up the application locally:

1. **Compile & Serialise the Classifiers**  
    ```bash
    python3 modelPickler.py
    ```

2. **Run the Application Server**
    ```bash
    python3 index.py
    ```

3. **View in Browser**  
   Open your preferred web browser and navigate to:  
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


## ☁️ Hosting on Render

Deploying to Render is highly recommended and practically straight-forward. 

When setting up your web service on Render, simply use the following run command:

    ```bash
    gunicorn index:app
    ```

---

## Deprecated 

### Hosting on Heroku (Not Free anymore)
1. Login to your heroku account on workspace using `heroku login` & then providing credentials.
2. Create the app using `heroku create <*NameOfApp*>` e.g `heroku create cricai`
3. Set Buildpacks for the app using `heroku buildpacks:set heroku/python`
4. Generate a file using `pip freeze > requirements.txt`
5. Create a file named *Procfile* with contents as `web: gunicorn index:app`
6. Commit the steps using `git add .` & then, `git commit -m "MESSAGE"`
7. Push for deploy using `git push heroku master`