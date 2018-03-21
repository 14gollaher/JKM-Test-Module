from django.shortcuts import render
from TangoComponents.TangoRepository import *
from TangoComponents.TangoUserApplication import *
from TangoComponents.TangoPermutationGenerator import *
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
            'field_names': json.dumps(list(tangoUserApplication.get_view_field_names(test_view_name)), cls = DjangoJSONEncoder)
        }
    )

def view_select(request):
    tangoUserApplication = TangoUserApplication()

    return render(
        request,
        'tango/view-select.html',
        {
            'views': json.dumps(list(tangoUserApplication.views), cls = DjangoJSONEncoder)
        }
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

def generate_permutations(request):
    tango_permutation_generator = TangoPermutationGenerator()
    tango_permutation_generator.generate_permutations(request.GET['viewName'])

    return JsonResponse(tango_permutation_generator.permutations, safe = False)