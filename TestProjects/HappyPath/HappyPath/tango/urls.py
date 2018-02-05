from django.conf.urls import include, url

import tango.views

urlpatterns = [
    url(r'^results', tango.views.results, name = "results"),
    url(r'^permutation', tango.views.get_permutations, name = "permutation"),
    url(r'^(?P<test_view_name>\w+|)', tango.views.testing, name = "testing")
]
