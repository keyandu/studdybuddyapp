
from re import template
from django.contrib.auth.models import User
from django.urls import resolve
from django.http import HttpResponse
from http.client import responses
from urllib import response
from django.shortcuts import render
from django.views.generic import DetailView, CreateView
# from .models import UserClass
import requests
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Profile, StudySessionModel, Class
from .forms import EditProfileForm, StudySessionForm
from django.forms import modelformset_factory
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import get_object_or_404
import json

def edit_profile(request, pk):
    # check if the user has a profile
    try:
        profile = request.user.profile
    except Profile.DoesNotExist: 
        # if user has no profile, create one
        profile = Profile(user=request.user)
    
    if request.method == 'POST':
        # set form instance to be the current user's profile
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect(reverse('user_profile', args=(pk,)))    
    else:
        form = EditProfileForm(instance=profile)

    return render(request, 'editProfile.html', {'form': form})


def friendslist(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'friendsList.html', context)


class profile(DetailView):
    model= Profile
    template_name ='profile.html'
    def get_object(self):
        return self.request.user


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
        result = list(filter(lambda x: (x['description'].upper().__contains__(query_name.upper()) or (x['subject']+" "+x['catalog_number']).upper().__contains__(query_name.upper()) or x['instructor']['name'].upper().__contains__(query_name.upper())), response))
        return render(request, 'search.html', {"result":result})
    return render(request, 'search.html',{"result":{"n"}})

# Add class to user profile's Enrolled Courses field.
# Triggered by 'Add' button on Course List page, classinfo.html.
def add_class(request):
    profile = request.user.profile
    if request.method == "POST":
        # Create new course
        subject = request.POST.get('subject')
        catalog_number = request.POST.get('catalog_number')
        course_number = request.POST.get('course_number')
        description = request.POST.get('description')
        instructor = request.POST.get('instructor')
        new_course = Class(subject_field=subject, catalog_number_field=catalog_number, course_number_field=course_number, description_field=description, instructor_field=instructor)
        # TODO: check if course exists already
        if not Class.objects.filter(course_number_field=course_number).exists():
            new_course.save()

        if not profile.Enrolled_Courses.filter(course_number_field=course_number).exists():
            profile.Enrolled_Courses.add(new_course)
            profile.save()
    return HttpResponseRedirect(reverse('user_profile', args=(profile.id,)))

#def create_class(subject, course_number):


class AddSessionView(CreateView):
    model = StudySessionModel
    template_name = 'study_session_post.html'
    fields = '__all__'
def post_list(request):
    formset = StudySessionModel.objects.all()
    return render(request, 'list.html',{'formset':formset})

class StudySessionDetailView(DetailView):
    model = StudySessionModel
    template_name = 'session_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(StudySessionDetailView, self).get_context_data(**kwargs)
        studysession = get_object_or_404(StudySessionModel,id=self.kwargs['pk'])
        context["enroll_list"] = studysession.enroll.all()
        return context
        
def EnrollView(request,pk):
    study_session = get_object_or_404(StudySessionModel, id=pk)
    study_session.enroll.add(request.user)
    return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))
    
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
