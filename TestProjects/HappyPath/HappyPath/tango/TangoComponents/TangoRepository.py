import os
import json
from tango.tinydb.database import TinyDB
from tango.tinydb.queries import Query, where



class TangoRepository:
    def __init__(self):
        self.directory = os.path.dirname(__file__) 
        self.filePath = os.path.join(self.directory, 'tango-cases.json')
        self.initialize_database()
        
    def initialize_database(self):
        self.database = TinyDB(self.filePath)

    def get_permutation(self, view_name):
        if not view_name: test_view_name = 'index'
        
        return self.database.table(view_name).all()

    def insert_cases(self, view_name, cases):
        if not view_name: view_name = 'index'

        table = self.database.table(view_name)
        table.insert_multiple(cases)