from flask import Flask

# Import the routes so Flask registers them
import routes

app = Flask(__name__)
		
		
if __name__ =='__main__':
	app.run(debug=True)