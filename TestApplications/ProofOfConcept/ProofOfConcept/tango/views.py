from django.shortcuts import render

def viewTest(request, viewToTest):
    if viewToTest is None:
        viewToTest = ''
    return render(
        request,
        'tango/index.html',
        {
            'viewToTest': viewToTest
        }
    )