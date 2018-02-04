from django.shortcuts import render

def viewTest(request, viewToTest):
    if viewToTest is None: viewToTest = ''
    return render(
        request,
        'tango/index.html',
        {
            'viewToTest': viewToTest
        }
    )
class TangoUserApplication:
    """description of class"""
    Model_Info = []

    def __init__(self):
        app_models = apps.get_app_config('app').get_models();
        for model in app_models:
            fields = model._meta.get_fields()
            for field in fields:
              if not field.is_relation or field.one_to_one or (field.many_to_one and field.related_model):
                  type = field.get_internal_type()
                  name = field.name
                  # what restrictions do we need to capture
                  max_length = field.max_length
                  ##create object here
                  model_tup = (type, name, max_length)
                  Model_Info.append(model_tup)

class TangoUserApplicationForm:

   
    def all_subclasses(self, cls):
        return cls.__subclasses__() + [g for s in cls.__subclasses__()
                                   for g in self.all_subclasses(s)]


    def __init__(self):
        self.ModelInfo = []
        all_forms = self.all_subclasses(django.forms.Form)
        x = all_forms[6]
        for row in x.base_fields.viewitems():
            name = row[0]
            kind = type(row[1])
            min = row[1].min_length;
            max = row[1].max_length;
            model_tup = (kind, name, min, max)
            
            self.ModelInfo.append(model_tup)