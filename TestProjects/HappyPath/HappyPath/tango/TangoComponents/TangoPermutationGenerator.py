import os
import json
from TangoUserApplication import *
from faker import Faker
from random import randint
import random


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
            elif type is TangoType.time: self.process_time_attribute(property)
            elif type is TangoType.url: self.process_url_attribute(property)
            elif type is TangoType.ipAddress: self.process_ipaddress_attribute(property)



    def process_ipaddress_attribute(self, property):
        permutation = {}
        permutation['name'] = property['name']
        permutation['selector'] = "#id_" + permutation['name'];
        permutation['test_values'] = []
        
        #Happy path example
        permutation['test_values'].append(self.fake.ipv6(network=False))
        permutation['test_values'].append(self.fake.ipv4(network=False))
        #add other ip address fomrujlas

        #support length later


        #Blank
        permutation['test_values'].append('') 
        self.permutations.append(permutation)


    def process_url_attribute(self, property):
        permutation = {}
        permutation['name'] = property['name']
        permutation['selector'] = "#id_" + permutation['name'];
        permutation['test_values'] = []
        
        #Happy path example
        permutation['test_values'].append(self.fake.uri())

        #support length later


        #Blank
        permutation['test_values'].append('') 
        self.permutations.append(permutation)


    def process_date_attribute(self, property):
        permutation = {}
        permutation['name'] = property['name']
        permutation['selector'] = "#id_" + permutation['name'];
        permutation['test_values'] = []
        
        #Happy path example
        permutation['test_values'].append(self.fake.date(pattern="%Y-%m-%d", end_datetime=None))
        permutation['test_values'].append(self.fake.date(pattern="%m-%d-%Y", end_datetime=None))
        permutation['test_values'].append(self.fake.date(pattern="%d-%m-%Y", end_datetime=None))


        #Blank
        permutation['test_values'].append('') 
        self.permutations.append(permutation)

    def process_time_attribute(self, property):
        permutation = {}
        permutation['name'] = property['name']
        permutation['selector'] = "#id_" + permutation['name'];
        permutation['test_values'] = []
        
        #Happy path example
        permutation['test_values'].append(self.fake.time(pattern="%H:%M:%S", end_datetime=None))
        #permutation['test_values'].append(self.fake.time(pattern="%h:%m:%s", end_datetime=None))
        #permutation['test_values'].append(self.fake.time(pattern="%s:%M:%H", end_datetime=None))



        #Blank
        permutation['test_values'].append('') 
        self.permutations.append(permutation)



    def process_decimal_attribute(self, property):
        permutation = {}
        permutation['name'] = property['name']
        permutation['selector'] = "#id_" + permutation['name'];
        permutation['test_values'] = []

        #Happy path example
        permutation['test_values'].append(self.fake.random_number()) 

        #Blank
        permutation['test_values'].append('') 

        #Maximum value
        if 'max_value' in property:
            abc = random.uniform(property['max_value'],property['max_value'] + 12.42)
            permutation['test_values'].append(abc)

        #minimum value
        if 'min_value' in property:
            abc = random.uniform(property['min_value'] - 42.21, property['min_value'])
            permutation['test_values'].append(random.uniform(property['min_value'] - 0.5, property['min_value']))
        
        #Zero
        permutation['test_values'].append('0') 

        #DecimalPlaces #TODO
        #if 'decimal_places' in property:
         #   permutation['test_values'].append(property['decimal_places'])
          #  permutation['test_values'].append(self.fake.finance.amount(fake.random_int(1,10000), fake.random_int(10001, 50000), property['decimal_places'] + 1))

        #MaxDigits #TODO
        #if 'max_digits' in property:
         #   permutation['test_values'].append(property['max_digits'])
          #  range_start = 10**(property['max_digits'])
           # range_end = (10**property['max_digits'])-1
           # permutation['test_values'] = randint(range_start, range_end)

        self.permutations.append(permutation)


    def process_float_attribute(self, property):
        permutation = {}
        permutation['name'] = property['name']
        permutation['selector'] = "#id_" + permutation['name'];
        permutation['test_values'] = []

        #Happy path example
        permutation['test_values'].append(self.fake.random_number()) 

        #Blank
        permutation['test_values'].append('') 

        #Maximum value
        if 'max_value' in property:
            abc = random.uniform(property['max_value'],property['max_value'] + 12.42)
            permutation['test_values'].append(abc)

        #minimum value
        if 'min_value' in property:
            abc = random.uniform(property['min_value'] - 42.21, property['min_value'])
            permutation['test_values'].append(random.uniform(property['min_value'] - 0.5, property['min_value']))
        
        #Zero
        permutation['test_values'].append('0') 
        
        self.permutations.append(permutation)





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

        ## True
        #permutation['test_values'].append(True)

        ## False
        #permutation['test_values'].append(False)

        ## Blank
        #permutation['test_values'].append('')

        self.permutations.append(permutation)