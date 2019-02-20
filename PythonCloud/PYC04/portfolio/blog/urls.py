#!usr/bin/env python
# -*- coding:utf-8 _*_
"""
@author:Chiu
@file: urls.py
@time: 2019/02/18

"""
from django.urls import path
from .views import *
urlpatterns = [
	path('', blog_page),
        path('<int:blog_id>/', blog_text)
]
