from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from forms import HappyPathForm, SadPathForm, SuperForm, ClassForm
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

def sample_view(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ClassForm()
        #form = HappyPathForm(auto_id="custom_%s")


    return render(request, 'sample-form.html', {'form': form})

def super_view(request):
    if request.method == 'POST':
        form = SuperForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = SuperForm()

    return render(request, 'sample-form.html', {'form': form})


def sad_view(request):
    if request.method == 'POST':
        form = SadPathForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = SadPathForm()

    return render(request, 'sample-form.html', {'form': form})