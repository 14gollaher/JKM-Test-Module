from django.apps import apps
import inspect
from django.conf import settings
from django.core.urlresolvers import RegexURLResolver, RegexURLPattern
import django
from app import views

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
        #TODO: should this be a configuration file thign?
        with open('C:/Tango/Tango/TestProjects/HappyPath/HappyPath/app/views.py') as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content] 
        listofcomments = [];
        modelsandviews = [];
        

        for line in content:
            if len(line) > 0 and line[0] == '#':
                listofcomments.append(line)

        for comment in listofcomments:
            if(comment.upper().find('#TANGO: ') != -1):
                individualViews = []
                parsedString = comment[8:]
                parsedString = parsedString.strip()

                spaceLocation = parsedString.find(' ')
                viewName = parsedString[0:spaceLocation]
                modelsAndFormsString = parsedString[spaceLocation+1:]

                modelsAndFormsString = modelsAndFormsString.strip()

                done = False
                while(done == False):
                    spaceLocation = modelsAndFormsString.find(' ')

                    if(spaceLocation != -1):
                        modelsandviews.append(modelsAndFormsString[0:spaceLocation])
                        modelsAndFormsString = modelsAndFormsString[spaceLocation+1:]

                    else:
                        modelsandviews.append(modelsAndFormsString)
                        done = True

                individualViews.append(viewName)
                

                for object in modelsandviews:
                    view_property = {}
                    view_property['name'] = object
                    view_property['type'] = 'unknown'
                    for model in self.models:
                       if(model[0] == object):
                          view_property['type'] = 'model'
                          break
                    for form in self.forms:
                       if(form[0] == object):
                          view_property['type'] = 'form'
                          break


                    individualViews.append(view_property)
            self.views.append(individualViews)




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

    from django.conf import settings
    from django.core.urlresolvers import RegexURLResolver, RegexURLPattern

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

