from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello world")
def home(request):
    return HttpResponse("<h1>welcome to home page</h1>")
def html_demo(request):
    return render(request,"sample1.html")
def html_demo1(request):
    return render(request,"sample2.html")