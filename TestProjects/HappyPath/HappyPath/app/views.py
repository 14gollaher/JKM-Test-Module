from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from forms import HappyPathForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title':'Home Page'
        }
    )

#Tango: sample_form HappyPathForm
def sample_form(request):
    if request.method == 'POST':
        form = HappyPathForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = HappyPathForm()

    return render(request, 'sample-form.html', {'form': form})
