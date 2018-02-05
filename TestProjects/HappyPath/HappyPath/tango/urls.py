from django.conf.urls import include, url

import tango.views

urlpatterns = [
    url(r'^results', tango.views.results, name = "results"),
    url(r'^generate-permutations', tango.views.generate_permutations, name = "generate_permutations"),
    url(r'^(?P<test_view_name>\w+|)', tango.views.testing, name = "testing")
]
