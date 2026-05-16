## Repository acts as sub repository to the base, serves the purpose of deployment & webhooks

https://cricai.onrender.com

### Build & Local setup
1. Clone the project using `git clone https://github.com/jaykay12/CricAI.git`
2. Explore into the Web-App using `cd CricAI/Web-App`
3. Create a Virtual Env using `python3 -m virtualenv venv`
4. Activate the Virtual Env using `source venv/bin/activate`
5. Install all dependencies using `pip install -r requirements.txt`

### Running on Local
1. Pickle Classifiers using `python3 modelPickler.py`
2. Run Model using `python3 index.py`
3. Open Browser & Hit `http://127.0.0.1:5000/`


### Hosting on Render
1. Almost straight-forward with the `gunicorn index:app` as run command.

## Deprecated

### Hosting on Heroku (Not Free anymore)
1. Login to your heroku account on workspace using `heroku login` & then providing credentials.
2. Create the app using `heroku create <*NameOfApp*>` e.g `heroku create cricai`
3. Set Buildpacks for the app using `heroku buildpacks:set heroku/python`
4. Generate a file using `pip freeze > requirements.txt`
5. Create a file named *Procfile* with contents as `web: gunicorn index:app`
6. Commit the steps using `git add .` & then, `git commit -m "MESSAGE"`
7. Push for deploy using `git push heroku master`