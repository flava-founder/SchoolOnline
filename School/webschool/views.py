from django.shortcuts import render
from webschool import models
from django.http import HttpResponse
def index(requests):
    return render(requests, "index.html")

def about(requests):
    return render(requests, "about.html")

def courses(requests):
    teachers = models.Teachers.objects.all()
    return render(requests, "courses.html" , context={"Teachers" : teachers })

def feedbacks(requsets):
    return render(requsets, "feedbacks.html")


