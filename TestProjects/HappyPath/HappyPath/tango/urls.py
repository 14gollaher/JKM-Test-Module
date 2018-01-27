from django.conf.urls import url

import tango.views

urlpatterns = [
    url(r'^(?P<viewToTest>\w+|)', tango.views.viewTest, name = "viewTest")
]

