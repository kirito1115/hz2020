from django.http import HttpResponse
from django.shortcuts import redirect
def index(request):
    return HttpResponse("hello world!")
def log(request):
    return redirect('/index')
