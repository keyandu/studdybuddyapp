from django.contrib.auth.models import User
from django.urls import resolve
from django.http import HttpResponse
from http.client import responses
from urllib import response
from django.shortcuts import render
# from .models import UserClass
import requests
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Profile, UserCourse, StudySessionModel
from .forms import EditProfileForm, StudySessionForm
from django.forms import modelformset_factory
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import get_object_or_404
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


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    url_name = resolve(request.path).url_name

    context = {
        'profile': profile,
        'url_name': url_name,
    }

    return render(request, 'profile.html', context)


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
    
def post_study_session(request):
    if request.method == 'POST':
        formset = StudySessionForm(request.POST)
        if formset.is_valid():
            #starttime = formset.cleaned_data['start_time']
           # newformset = StudySessionModel(start_time = starttime)
            formset.save()
    else:
        formset = StudySessionForm()
    return render(request, 'study_session_post.html',{'formset':formset})

def list(request):
    studyForm = modelformset_factory(StudySessionModel, fields=('title','text','start_time','author',))
    formset = studyForm(queryset = StudySessionModel.objects.all())
    return render(request, 'list.html',{'formset':formset})

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
