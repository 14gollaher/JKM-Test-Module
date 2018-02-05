from django.shortcuts import render
from TangoComponents.TangoRepository import *
from TangoComponents.TangoUserApplication import *
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

def testing(request, test_view_name):

    if test_view_name is None: test_view_name = ''

    tangoUserApplication = TangoUserApplication()

    return render(
        request,
        'tango/testing.html',
        {
            'test_view_name': test_view_name,
            'forms': json.dumps(list(tangoUserApplication.forms), cls = DjangoJSONEncoder)
        }
    )

def results(request):
    return render(
        request,
        'tango/results.html'
    )

def get_permutations(request):
    tangoRepository = TangoRepository()
    permutations = tangoRepository.get_test_permutations('index')
    return JsonResponse(permutations, safe = False)