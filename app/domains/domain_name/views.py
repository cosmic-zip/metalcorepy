from django.shortcuts import render
from domains.domain_name.opa import *
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")
