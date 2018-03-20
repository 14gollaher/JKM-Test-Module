from django.apps import apps
import inspect
from django.conf import settings
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern
import django
from app import views
import app
import os
import json


class TangoUserApplication:
    def __init__(self):
        self.populate_models()
        self.populate_forms()
        self.populate_views()

    #format for comments should be '#TANGO: <Name of View> <ModelorForm> <ModelorForm>....
    #for example
    #TANGO: sampleview samplemodel1 sampleform1 sampleform2
    #would be a view with 1 model and 2 forms on it
    #thought it would be easier to just let them list them, as i can determine from code if they something is a model or form
    
    def populate_views(self):
        self.views = []
        file_path = os.path.join(os.path.dirname(__file__)) + '\\TangoConfiguration.json'
        
        with open(file_path) as data_file:    
            settings = json.load(data_file)

        for view, view_value in settings['views-to-test'].iteritems():
            new_view = {}
            new_view['name'] = view
            new_view['components'] = []
            for view_or_model in view_value:
                view_component = {}
                view_component['name'] = view_or_model
                for model in self.models:
                    if(model[0] == view_or_model):
                        view_component['type'] = 'model'
                        break
                for form in self.forms:
                    if(form[0] == view_or_model):
                        view_component['type'] = 'form'
                        break
                new_view['components'].append(view_component)
            self.views.append(new_view)

    def populate_models(self):
        self.models = [];
        models = apps.get_app_config('app').get_models();
        for model in models:
            eachmodel = [];
            eachmodel.append(model.__name__)
            fields = model._meta.get_fields()
            for field in fields:
              if not field.is_relation or field.one_to_one or (field.many_to_one and field.related_model):
                  model_property = {}
                  model_property['tango_name'] = field.get_internal_type()
                  model_property['tango_type'] = field.name
                  model_property['max_length'] = field.max_length

                  eachmodel.append(model_property)
            self.models.append(eachmodel)


    def populate_forms(self):
        self.forms = []

        all_forms = self.get_subclasses(django.forms.Form) 
        happyPathForm = all_forms[6] 
        
        for row in happyPathForm.base_fields.viewitems():
            form_property = {}
            form_property['tango_name'] = row[0]
            form_property['tango_type'] = self.get_tango_type((row[1]))
            form_property['tango_selector'] = "#id_" + form_property['tango_name']

        for x in range(6, len(all_forms) - 1): 
            thisform = all_forms[x];
            forms = []
            forms.append(thisform.__name__)
            for row in thisform.base_fields.viewitems():
                form_property = {}
                form_property['tango_name'] = row[0]
                form_property['tango_selector'] = "#id_" + form_property['tango_name']
                form_property['tango_type'] = self.get_tango_type((row[1]))
                if hasattr(row[1], 'max_length'): 
                    form_property['max_length'] = row[1].max_length
                if hasattr(row[1], 'min_length') and row[1].min_length: 
                    form_property['min_length'] = row[1].min_length

                forms.append(form_property)
            self.forms.append(forms)


    def get_tango_type(self, djangoType):
        if type(djangoType) is django.forms.fields.CharField: return TangoType.string
        if type(djangoType) is django.forms.fields.EmailField: return TangoType.email
        if type(djangoType) is django.forms.fields.IntegerField: return TangoType.integer
        if type(djangoType) is django.forms.fields.DateField: return TangoType.date
        if type(djangoType) is django.forms.fields.DateTimeField: return TangoType.date_time
        if type(djangoType) is django.forms.fields.FloatField: return TangoType.float
        if type(djangoType) is django.forms.fields.Decimal: return TangoType.decimal
        if type(djangoType) is django.forms.fields.BooleanField: return TangoType.boolean

    def get_subclasses(self, cls): 
        return cls.__subclasses__() + [g for s in cls.__subclasses__() 
                                   for g in self.get_subclasses(s)] 

    def get_all_subclasses(self, parent_class):
        all_subclasses = []

        for subclass in parent_class.__subclasses__():
            all_subclasses.append(subclass)
            all_subclasses.extend(get_all_subclasses(subclass))

        return all_subclasses


class TangoType:
    string = 1
    email = 2
    integer = 3
    date_time = 4
    date = 5
    decimal = 6
    float = 7
    boolean = 8

