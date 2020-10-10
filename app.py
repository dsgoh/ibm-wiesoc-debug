#!flask/bin/python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
	return "covid link safe community transmission?"

if __name__ == '__main__':
	app.run(debug=True)