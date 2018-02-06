from django.shortcuts import render
from TangoComponents.TangoRepository import *
from TangoComponents.TangoUserApplication import *
from TangoComponents.TangoPermutationGenerator import *
from django.http import JsonResponse
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
            'form': json.dumps(list(tangoUserApplication.forms[0]), cls = DjangoJSONEncoder)
        }
    )

def results(request):
    return render(
        request,
        'tango/results.html'
    )

def get_permutations(request):
    tango_repository = TangoRepository()
    permutations = tangoRepository.get_test_permutations('index')
    return JsonResponse(permutations, safe = False)

def generate_permutations(request):
    form = ast.literal_eval(request.GET['form'])

    tango_permutations_generator = TangoPermutationGenerator()
    tango_permutations_generator.process_form(form)

    return JsonResponse(tango_permutations_generator.permutations)