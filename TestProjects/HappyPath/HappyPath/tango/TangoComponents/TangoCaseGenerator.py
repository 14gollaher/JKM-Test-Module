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
            elif type is TangoType.date: self.process_date_attribute(property)
            elif type is TangoType.date_time: self.process_date_time_attribute(property)
            elif type is TangoType.decimal: self.process_decimal_attribute(property)
            elif type is TangoType.float: self.process_float_attribute(property)
            elif type is TangoType.boolean: self.process_boolean_attribute(property)


    def process_string_attribute(self, property):
        name = property['tango_name']
        self.cases[name] = []

        # Happy path example
        self.cases[name].append(self.fake.text(max_nb_chars=25, ext_word_list=None))

        # BLANK
        self.cases[name].append('');

        # SQL
        self.cases[name].append(self.fake.first_name() + " OR 1=1")

        # Maximum length 
        if 'max_length' in property:
            self.cases[name].append(self.fake.pystr(property['max_length'], property['max_length'] ))
            self.cases[name].append(self.fake.pystr(property['max_length'] + 1, property['max_length'] + 1))

        # Minimum length 
        if 'min_length' in property:
            self.cases[name].append(self.fake.pystr(property['min_length'], property['min_length'] ))
            self.cases[name].append(self.fake.pystr(property['min_length'] - 1, property['min_length'] - 1))

    def process_integer_attribute(self, property):
        name = property['tango_name']
        self.cases[name] = []

        # Happy path example
        self.cases[name].append(self.fake.random_number()) 
        
        # Blank
        self.cases[name].append('') 

        # SQL
        self.cases[name].append(self.fake.first_name() + " OR 1=1")

        # Minimum value
        if 'min_length' in property:
            self.cases[name].append(property['min_value'])
            self.cases[name].append(fake.random_int(min=property['min_value'] - 1, max=property['min_value'] - 1))

        # Maximum value
        if 'max_length' in property:
            self.cases[name].append(property['max_value'])
            self.cases[name].append(fake.random_int(min=property['max_value'] + 1, max=property['max_value'] + 1))

    def process_email_attribute(self, property):
        name = property['tango_name']
        self.cases[name] = []

        # Happy path
        self.cases[name].append(self.fake.free_email())

        # Blank
        self.cases[name].append('')

        # Company email
        self.cases[name].append(self.fake.company_email())

        # Email ending only
        self.cases[name].append(self.fake.tld())

        # SQL
        self.cases[name].append(self.fake.free_email() + " OR 1=1")

    def process_boolean_attribute(self, property):
        name = property['tango_name']
        self.cases[name] = []

        # True
        self.cases[name].append(True)

        # False
        self.cases[name].append(False)

        # Blank
        self.cases[name].append('')

