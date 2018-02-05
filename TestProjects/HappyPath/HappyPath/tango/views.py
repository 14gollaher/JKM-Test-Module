from django.shortcuts import render
from TangoComponents.TangoRepository import *
from TangoComponents.TangoUserApplication import *
from django.http import JsonResponse

def viewTest(request, viewToTest):
    if viewToTest is None: viewToTest = ''

    tangoUserApplication = TangoUserApplication();

    return render(
        request,
        'tango/testing.html',
        {
            'viewToTest': viewToTest
        }
    )

def viewResults(request):
    return render(
        request,
        'tango/results.html'
    )

def getPermutations(request):
    tangoRepository = TangoRepository()
    permutations = tangoRepository.get_test_permutations()
    return JsonResponse(permutations, safe = False)