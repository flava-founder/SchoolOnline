from django.shortcuts import render
from django.http import HttpResponse
def index(requsets):
    return HttpResponse("Hello")
