from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from forms import HappyPathForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title':'Home Page'
        }
    )

def sampleForm(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'sampleForm.html', {'form': HappyPathForm})
