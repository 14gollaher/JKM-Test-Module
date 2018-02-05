"""
Definition of urls for HappyPath.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views

import app.forms
import app.views
import tango.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^tango/', include('tango.urls', namespace="tango")),
    url(r'^$', app.views.home, name='home'),
    url(r'^sampleForm', app.views.sampleForm, name='sampleForm')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
