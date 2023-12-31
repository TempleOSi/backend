# Final Project: Web Application
# Authors:
#          A01746664 Eduardo Joel Cortez Valente
'''
This file consists of the definition of the General class wich is in charge of handling the requests and responses of the API.
'''

from factory.validation import Validator
from factory.database import Database

class General(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()
        
        self.collection_name = "General-Test"
        
        self.fields = {
            "name": "string",
            "body": "string",
            "created": "datetime",
            "updated": "datetime"
        }
        
        self.create_required_fields = ["title", "body"]

        # Fields optional for CREATE
        self.create_optional_fields = []

        # Fields required for UPDATE
        self.update_required_fields = ["title", "body"]

        # Fields optional for UPDATE
        self.update_optional_fields = []
        
    def create(self, todo):
        # Validator will throw error if invalid
        self.validator.validate(todo, self.fields, self.create_required_fields, self.create_optional_fields)
        res = self.db.insert(todo, self.collection_name)
        return "Inserted Id " + res

    def find(self, todo):  # find all
        return self.db.find(todo, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, todo):
        self.validator.validate(todo, self.fields, self.update_required_fields, self.update_optional_fields)
        return self.db.update(id, todo,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)
        