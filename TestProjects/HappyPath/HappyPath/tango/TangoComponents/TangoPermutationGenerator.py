import os
import json
from TangoUserApplication import *
from faker import Faker

class TangoPermutationGenerator:
    def __init__(self):
        self.permutations = []
        self.fake = Faker()

    def generate_permutations(self, test_view_name):
        tangoUserApplication = TangoUserApplication()

        for view in tangoUserApplication.views:
            if view['name'] == test_view_name:
                test_view = view
                break

        associated_forms = []
        associated_models = []
        
        for component in test_view['components']:
            for form in tangoUserApplication.forms:
                if form['name'] == component['name']:
                    self.generate_form_permutations(form['properties'])
                    break
            for model in tangoUserApplication.models:
                pass # TODO

    def generate_form_permutations(self, properties):
        for property in properties:
            type = property['type']
            if type is TangoType.string: self.process_string_attribute(property)
            elif type is TangoType.email: self.process_email_attribute(property)
            elif type is TangoType.integer: self.process_integer_attribute(property)
            elif type is TangoType.date: self.process_date_attribute(property)
            elif type is TangoType.date_time: self.process_date_time_attribute(property)
            elif type is TangoType.decimal: self.process_decimal_attribute(property)
            elif type is TangoType.float: self.process_float_attribute(property)
            elif type is TangoType.boolean: self.process_boolean_attribute(property)

    def process_string_attribute(self, property):
        permutation = {}
        permutation['name'] = property['name']
        permutation['selector'] = "#id_" + permutation['name'];
        permutation['test_values'] = []

        # Happy path example
        permutation['test_values'].append(self.fake.text(max_nb_chars=25, ext_word_list=None))

        # BLANK
        permutation['test_values'].append('');

        # SQL
        permutation['test_values'].append(self.fake.first_name() + " OR 1=1")

        # Maximum length 
        if 'max_length' in property:
            permutation['test_values'].append(self.fake.pystr(property['max_length'], property['max_length'] ))
            permutation['test_values'].append(self.fake.pystr(property['max_length'] + 1, property['max_length'] + 1))

        # Minimum length 
        if 'min_length' in property:
            permutation['test_values'].append(self.fake.pystr(property['min_length'], property['min_length'] ))
            permutation['test_values'].append(self.fake.pystr(property['min_length'] - 1, property['min_length'] - 1))

        self.permutations.append(permutation)
        
    def process_integer_attribute(self, property):
        permutation = {}
        permutation['name'] = property['name']
        permutation['selector'] = "#id_" + permutation['name']
        permutation['test_values'] = []

        # Happy path example
        permutation['test_values'].append(self.fake.random_number()) 
        
        # Blank
        permutation['test_values'].append('') 

        # SQL
        permutation['test_values'].append(self.fake.first_name() + " OR 1=1")

        # Minimum value
        if 'min_length' in property:
            permutation['test_values'].append(property['min_value'])
            permutation['test_values'].append(fake.random_int(min=property['min_value'] - 1, max=property['min_value'] - 1))

        # Maximum value
        if 'max_length' in property:
            permutation['test_values'].append(property['max_value'])
            permutation['test_values'].append(fake.random_int(min=property['max_value'] + 1, max=property['max_value'] + 1))

        self.permutations.append(permutation)

    def process_email_attribute(self, property):
        permutation = {}
        permutation['name'] = property['name']
        permutation['selector'] = "#id_" + permutation['name'];
        permutation['test_values'] = []

        # Happy path
        permutation['test_values'].append(self.fake.free_email())

        # Blank
        permutation['test_values'].append('')

        # Company email
        permutation['test_values'].append(self.fake.company_email())

        # Email ending only
        permutation['test_values'].append(self.fake.tld())

        # SQL
        permutation['test_values'].append(self.fake.free_email() + " OR 1=1")

        self.permutations.append(permutation)

    def process_boolean_attribute(self, property):
        permutation = {}
        permutation['name'] = property['name']
        permutation['selector'] = "#id_" + permutation['name'];
        permutation['test_values'] = []

        # True
        permutation['test_values'].append(True)

        # False
        permutation['test_values'].append(False)

        # Blank
        permutation['test_values'].append('')

        self.permutations.append(permutation)