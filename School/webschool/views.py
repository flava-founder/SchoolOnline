from django.shortcuts import render
from django.http import HttpResponse
def index(requests):
    return render(requests, "index.html")

def about(requests):
    return render(requests, "about.html")

def courses(requests):
    return render(requests, "courses.html")

def feedbacks(requsets):
    return render(requsets, "feedbacks.html")


