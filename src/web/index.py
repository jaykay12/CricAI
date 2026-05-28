from flask import Flask
from flask import request, render_template

# Import the routes so Flask registers them
from web.app.routes import main		

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.register_blueprint(main)

if __name__ =='__main__':
	app.run(debug=True, port=5000)