# Final Project: Web Application
# Authors:
#          A01746664 Eduardo Joel Cortez Valente
'''
This file consists of the definition of the Controller class wich is in charge of handling the requests and responses of the API.
'''
from flask import Flask, request


class Controller():

    def __init__(self):
        self.app = Flask(__name__)
        # CORS(self.app, resources={r"/*": {"origins": "*"}})
        self.app.route('/')(self.test)

    def test(self):
        print("Hello World!")
        return "Hello World!"
    
    def run(self):
        self.app.run(host='0.0.0.0', port=5000, debug=True)