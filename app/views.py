
from re import template
from django.contrib.auth.models import User
from django.urls import resolve
from django.http import HttpResponse
from http.client import responses
from urllib import response
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView
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
from django.db.models import Q

def edit_profile(request, pk):
    # Check if the user has a profile:
    try:
        profile = request.user.profile
    except Profile.DoesNotExist: 
        # If user has no profile, create one.
        profile = Profile(user=request.user)
    
    if request.method == 'POST':
        # Set form instance to be the current user's profile.
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
        # Course numbers are unique -- use it to check if course exists.
        course_number = request.POST.get('course_number')
        
        # If course does not already exist, create it.
        if not Class.objects.filter(course_number_field=course_number).exists():
            subject = request.POST.get('subject')
            catalog_number = request.POST.get('catalog_number')
            description = request.POST.get('description')
            instructor = request.POST.get('instructor')
            new_course = Class(subject_field=subject, catalog_number_field=catalog_number, 
                course_number_field=course_number, description_field=description, instructor_field=instructor)
            new_course.save()
        else:
            # Otherwise, get the existing instance.
            new_course = Class.objects.get(course_number_field=course_number)

        # Add the course to the user profile if it isn't already there.
        if not profile.Enrolled_Courses.filter(course_number_field=course_number).exists():
            profile.Enrolled_Courses.add(new_course)
            profile.save()
    return HttpResponseRedirect(reverse('user_profile', args=(profile.id,)))


class AddSessionView(CreateView):
    model = StudySessionModel
    form_class = StudySessionForm
    template_name = 'study_session_post.html'

    #fields = '__all__'

class UpadateSessionView(UpdateView):
    model = StudySessionModel
    template_name = 'editStudySession.html'
    fields = ['title','text','start_time','address','class_name']

def get_user_search(request):
    if request.method == "POST":
        query_name = request.POST.get('name')
        # user = get_object_or_404(User, username=query_name)
        try:
            user = User.objects.get(username=query_name)
        except User.DoesNotExist:
            user = None
        
        user_filter = Profile.objects.filter(Q(user=user) | Q(Major__contains=query_name) 
            | Q(Age__contains=query_name) | Q(Enrolled_Courses__subject_field__contains=query_name) 
            | Q(Enrolled_Courses__catalog_number_field__contains=query_name))
        return render(request, 'userSearch.html', {"u_filter": user_filter})

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
    
def EnrolledSessionsView(request):
    user = User.objects.get(username=request.user.username)
    enrolled = user.user_enroll.all()
    return render(request, 'index.html', {"enroll":enrolled})

def ListMyPostSessions(request):
    user = User.objects.get(username=request.user.username)
    my_posts = StudySessionModel.objects.filter(author=user)
    return render(request,'my_post_sessions.html',{"m_posts":my_posts})

def user_list(request):
    userList = Profile.objects.all()
    context = {'userList': userList}
    return render(request, 'userList.html', context)


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
