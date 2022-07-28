from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Home Page')
def Home(request):
    return render(request,'Home.html')


def djangoTest(request):
    return HttpResponse('hello sudhir')

def djangoTest1(request):
    return HttpResponse("<h1>welocme python</h2>")

def djangoTest2(request):
    a = 10+10
    return HttpResponse(a)

def djangoTest3(request):
    value='sudhir'
    return HttpResponse(value)


