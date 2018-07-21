#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^index$', views.index, name='home'),
]