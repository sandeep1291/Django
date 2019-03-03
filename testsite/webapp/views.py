# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<title>Vinay Yelluri</title><h1><center>Vinay Yelluri </center></h1>")


# Create your views here.
