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
    url(r'^sample-view', app.views.sample_view, name='sample_view'),
    url(r'^sad-view', app.views.sad_view, name='sad_view'),
    url(r'^super-view', app.views.super_view, name='super_view')
]