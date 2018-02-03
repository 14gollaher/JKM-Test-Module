from django.shortcuts import render
def viewTest(request, viewToTest):
    if viewToTest is None: viewToTest = ''
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