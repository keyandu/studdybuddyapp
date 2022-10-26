
from django.http import HttpResponse
from http.client import responses
from urllib import response
from django.shortcuts import render
# from .models import UserClass
import requests
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from app.models import Profile




@login_required

def profile(request):

    return render(request, 'profile.html')

def index(request):
    return HttpResponse("Hello, world. You're at the app page.")


def get_class(request):
    url = "http://luthers-list.herokuapp.com/api/dept/CS/"
    response = requests.get(url).json()
    return render(request, 'classinfo.html', {'response': response})

def get_search(request):
    if request.method == "POST":
        query_name = request.POST.get('name')
        response = requests.get("http://luthers-list.herokuapp.com/api/dept/CS/").json()
        result = list(filter(lambda x: x['description']==query_name, response))
        return render(request, 'search.html', {"result":result})
    return render(request, 'search.html',{"result":{"n"}})
    


#https://dev.to/earthcomfy/django-user-profile-3hik

# def submit(request):
#     description_text = request.POST.get('Class Name')
#     course_number_text = request.POST.get('Course Number')
#     instructor_text = request.POST.get('Instructor')
#     thought = UserClass(description_field=decsription_text, course_number_field=course_number_text, instructor_field=instructor_text)
#     thought.save()
#     # Always return an HttpResponseRedirect after successfully dealing
#     # with POST data. This prevents data from being posted twice if a
#     # user hits the Back button.
#     return HttpResponseRedirect('/class')
