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
def html_demo2(request):
    return render(request,"sample3.html",context={'data':"chandu",'name':"mouli"})
def html_demo3(request):
    fruits=["banana","mango","kiwi","orange"]
    return render(request,"sample4.html",{"fruits":fruits})

def html_demo4(request):
    return render(request,"sample5.html",{'a':10,'b':20})
def ab(request, ab):
    gre = list(map(int, ab.split(" ")))
    return HttpResponse(f"<h1>Maximum num is: {max(gre)}</h1>")
def gre(request,num):
    a=num.split(" ")
    if int(a[0])>int(a[1]):
        gre=int(a[0])
    else:
        gre=int(a[1])
    res=gre
    return HttpResponse(str(res))

def add(request,num):
    num=num.split(" ")
    res=int(num[0])+int(num[1])
    return HttpResponse(f"<h1>THE SUM IS : {str(res)}</H1>")

def add1(request,a,b):
    res=int(a)+int(a)
    return HttpResponse(res)