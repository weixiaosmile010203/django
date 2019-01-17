#!usr/bin/env python
# -*- coding:utf-8 _*_
"""
@author:Chiu
@file: urls.py
@time: 2019/01/10

"""

from django.urls import path
from . import views

urlpatterns = {
	path('', views.msgproc)
}