# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns=[
        path("test2app/", views.index, name="index")
        ]