import os
import json
from TangoUserApplication import *
from faker import Faker

class TangoPermutationGenerator:
    def __init__(self, form):
        self.permutations = {}
        self.fake = Faker()
        self.process_form(form)

    def process_form(self, form):
        for property in form:
            type = property['type']
            type = TangoType.email # delete me
            if type is TangoType.string: self.process_string_attribute(property)
            elif type is TangoType.email: self.process_email_attribute(property)
            elif type is TangoType.integer: self.process_integer_attribute(property)

    def process_string_attribute(self, property):
        name = property['name']
        self.permutations[name] = []

        # Happy path example
        self.fake = Faker('en-US')
        self.permutations[name].append(self.fake.first_name())

        # Chinese email
        self.fake = Faker('zh_CN')
        self.permutations[name].append(self.fake.first_name())

        # SQL
        self.permutations[name].append(self.fake.first_name() + " OR 1=1")

    def process_integer_attribute(self, property):
        name = property['name']
        self.permutations[name] = []

        # Happy path example
        self.permutations.append(faker.random.number(100)) 
        
        # SQL
        self.fake = Faker('en-US')
        self.permutations[name].append(self.fake.first_name() + " OR 1=1")

    def process_email_attribute(self, property):
        name = property['name']
        self.permutations[name] = []

        # Happy path example
        self.fake = Faker('en-US')
        self.permutations[name].append(self.fake.free_email())

        # Chinese email
        self.fake = Faker('zh_CN')
        self.permutations[name].append(self.fake.free_email())

        # SQL
        self.fake = Faker('en-US')
        self.permutations[name].append(self.fake.free_email() + " OR 1=1")
