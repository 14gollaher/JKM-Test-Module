import os
import json
from TangoUserApplication import *
from faker import Faker

class TangoCaseGenerator:
    def __init__(self):
        self.cases = {}
        self.fake = Faker()

    def process_form_cases(self, form):
        for property in form:
            type = property['tango_type']
            if type is TangoType.string: self.process_string_attribute(property)
            elif type is TangoType.email: self.process_email_attribute(property)
            elif type is TangoType.integer: self.process_integer_attribute(property)


    def process_string_attribute(self, property):
        name = property['tango_name']
        self.cases[name] = []

        # Happy path example
        #self.cases[name].append(self.fake.text(max_nb_chars=25, ext_word_list=None))

        # SQL
        self.cases[name].append(self.fake.first_name() + " OR 1=1")

        if property['max_length']:
            self.cases[name].append(self.fake.pystr(property['max_length'] + 1, property['max_length'] + 1))

    def process_integer_attribute(self, property):
        name = property['tango_name']
        self.cases[name] = []

        # Happy path example
        self.cases[name].append(self.fake.random_number(5)) 
        
        # SQL
        self.cases[name].append(self.fake.first_name() + " OR 1=1")

    def process_email_attribute(self, property):
        name = property['tango_name']
        self.cases[name] = []

        # Happy path example
        self.cases[name].append(self.fake.free_email())

        # Chinese email
        self.fake = Faker('zh_CN')
        self.cases[name].append(self.fake.free_email())
        self.fake = Faker('en-US')

        # SQL
        self.cases[name].append(self.fake.free_email() + " OR 1=1")
