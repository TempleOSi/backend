# Final Project: Web Application
# Authors:
#          A01746664 Eduardo Joel Cortez Valente
'''
This file consists of the definition of the Controller class wich is in charge of handling the requests and responses of the API.
'''

from flask import Flask, request, jsonify
from models import general
from flask_cors import CORS

class Controller():

    def __init__(self):
        self.app = Flask(__name__)
        self.general = general.General()
        CORS(self.app, resources={r"/*": {"origins": "*"}})
        
        # Routes
        self.app.route('/test')(self.test)
        self.app.route('/getAllGeneral', methods=['GET'])(self.getAllGeneral)
        self.app.route('/addGeneral', methods=['POST'])(self.addGeneral)
        self.app.route('/getOneGeneral/<id>', methods=['GET'])(self.getOneGeneral)
        self.app.route('/updateGeneral/<id>', methods=['PUT'])(self.updateGeneral)
        self.app.route('/deleteGeneral/<id>', methods=['DELETE'])(self.deleteGeneral)

    def test(self):
        print("Hello World!")
        return "Hello World!"
    
    def getAllGeneral(self):
        return jsonify(self.general.find({})), 200
    
    def getOneGeneral(self, id):
        return jsonify(self.general.find_by_id(id)), 200
    
    def addGeneral(self):
        if request.method == "POST":
            title = request.get_json()['title']
            body = request.get_json()['body']
            response = self.general.create({'title': title, 'body': body})
            return response, 201
    
    def updateGeneral(self, id):
        if request.method == "PUT":
            title = request.get_json()['title']
            body = request.get_json()['body']
            response = self.general.update(id, {'title': title, 'body': body})
            return response, 201
        
    def deleteGeneral(self, id):
        if request.method == "DELETE":
            response = self.general.delete(id)
            return response, 201
    
    def run(self):
        self.app.run(host='0.0.0.0', port=5000, debug=True)