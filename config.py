# Final Project: Web Application
# Authors:
#          A01746664 Eduardo Joel Cortez Valente
'''
This file consists of the definition of the Database class wich is in charge of handling the connection to the database.
'''

import json

config = json.load(open('db_config.json'))  #load db in json format
