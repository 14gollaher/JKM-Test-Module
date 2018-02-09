from django.conf.urls import include, url

import tango.views

urlpatterns = [
    url(r'^generate-cases', tango.views.generate_cases, name = "generate_cases"),
    url(r'^save-cases', tango.views.save_cases, name = "save_cases"),
    url(r'^get-cases', tango.views.get_cases, name = "get_cases"),
    url(r'^(?P<test_view_name>\'?\w+([-]\w+)*\'?)', tango.views.testing, name = "testing")
]
