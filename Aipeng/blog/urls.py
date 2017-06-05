#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ""
__author__ = "admin"
__mtime__ = "2017-06-05"
"""

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.index),
]