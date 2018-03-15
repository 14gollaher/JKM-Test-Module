from django.shortcuts import render
from TangoComponents.TangoRepository import *
from TangoComponents.TangoUserApplication import *
from TangoComponents.TangoCaseGenerator import *
from django.http import JsonResponse, HttpResponse
import json
import ast
from django.core.serializers.json import DjangoJSONEncoder

def testing(request, test_view_name):
    if test_view_name is None: test_view_name = ''

    tangoUserApplication = TangoUserApplication()
    return render(
        request,
        'tango/testing.html',
        {
            'test_view_name': test_view_name,
            #TODO: Don't want to call forms[0] here anymore, need to pick form based on test_view_name
            # so we probably want a populate_views method
            'form': json.dumps(list(tangoUserApplication.forms[0]), cls = DjangoJSONEncoder)
        }
    )

def results(request):
    return render(
        request,
        'tango/results.html'
    )

def save_cases(request):
    view_name = request.GET['viewName']
    cases = ast.literal_eval(request.GET['cases'])

    tango_repository = TangoRepository()
    tango_repository.insert_cases(view_name, cases)
    return HttpResponse('')

def get_cases(request):
    view_name = request.GET['viewName']

    tango_repository = TangoRepository()
    cases = tango_repository.get_cases(view_name)
    return JsonResponse(cases,  safe = False)

def generate_cases(request):
    form = ast.literal_eval(request.GET['form'])

    tango_cases_generator = TangoCaseGenerator()
    tango_cases_generator.process_form_cases(form)

    return JsonResponse(tango_cases_generator.cases)