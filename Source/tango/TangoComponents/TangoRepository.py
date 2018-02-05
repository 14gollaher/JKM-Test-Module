import os
import json
from tango.tinydb.database import TinyDB
from tango.tinydb.queries import Query

class TangoRepository:
    def __init__(self):
        self.directory = os.path.dirname(__file__) 
        self.filePath = os.path.join(self.directory, 'tango-permutations.json')
        self.create_database()

    def get_test_permutations(self):
        with open(self.filePath, 'r') as file:
            return json.load(file)

    def create_database(self):
        db = TinyDB(self.filePath)
        x = 5
        #file = open(self.filePath, "w+")
        #file.close() 
