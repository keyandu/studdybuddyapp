from django.http import HttpResponse
from http.client import responses
from urllib import response
from django.shortcuts import render
import requests

def index(request):
    return HttpResponse("Hello, world. You're at the app page.")
    
def get_class(request):
    url = "http://luthers-list.herokuapp.com/api/dept/CS/"
    response = requests.get(url).json()
    return render(request,'app/classinfo.html',{'response':response})
