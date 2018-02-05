from django.apps import apps
import django

class TangoUserApplication:
    def __init__(self):
        self.populate_models()
        self.populate_forms()

    def populate_models(self):
        models = apps.get_app_config('app').get_models();
        for model in models:
            fields = model._meta.get_fields()
            for field in fields:
              if not field.is_relation or field.one_to_one or (field.many_to_one and field.related_model):
                  type = field.get_internal_type()
                  name = field.name
                  max_length = field.max_length

                  model_tuple = (type, name, max_length)
                  self.model_info.append(model_tup)

    # TODO: Make forms be a list of form, and make it not need any "Hardcoding"
    def populate_forms(self):
        self.forms = []

        all_forms = self.get_subclasses(django.forms.Form) 
        happyPathForm = all_forms[6] 
        for row in happyPathForm.base_fields.viewitems():
            form = {}
            form['name'] = row[0]
            form['kind'] = self.get_tango_type((row[1]))
            #min = row[1].min_length; 
            #max = row[1].max_length; 
            #model_tup = (kind, name, min, max) 
            self.forms.append(form)

    def get_tango_type(self, djangoType):
        if type(djangoType) is django.forms.fields.CharField: return TangoType.string
        if type(djangoType) is django.forms.fields.EmailField: return TangoType.email
        if type(djangoType) is django.forms.fields.IntegerField: return TangoType.integer

    def get_subclasses(self, cls): 
        return cls.__subclasses__() + [g for s in cls.__subclasses__() 
                                   for g in self.get_subclasses(s)] 
 
class TangoType:
    string = 1
    email = 2
    integer = 3
 

