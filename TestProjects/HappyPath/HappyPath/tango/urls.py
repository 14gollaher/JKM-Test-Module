from django.conf.urls import include, url

import tango.views

urlpatterns = [
    url(r'^results', tango.views.viewResults, name = "results"),
    url(r'^permutations', tango.views.getPermutations, name = "permutations"),
    url(r'^(?P<viewToTest>\w+|)', tango.views.viewTest, name = "viewTest")
]
