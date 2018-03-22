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
    url(r'^tango/', include('tango.urls', namespace="tango")),
    url(r'^$', app.views.home, name='home'),
    url(r'^sample-form', app.views.sample_form, name='sample_form'),
    url(r'^sad-form', app.views.sad_form, name='sad_form'),
    url(r'^super-form', app.views.super_form, name='super_form')
]