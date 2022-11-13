from allauth.account.forms import SignupForm
from django.forms import ModelForm
from .models import Profile, StudySessionModel, Class
from django import forms
from django.contrib.auth.models import User

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['Age', 'Major', 'Enrolled_Courses', 'Bio']


class SignupProfileForm(SignupForm):
    class Meta:
        model = Profile
        fields = ['Age', 'Major', 'Enrolled_Courses', 'Bio']

        def save(self, request):
            # Ensure you call the parent class's save.
            # .save() returns a User object.
            user = super(SignupProfileForm, self).save(request)

            # Add your own processing here.

            # You must return the original result.
            return user


class StudySessionForm(ModelForm):
    class Meta:
        model = StudySessionModel
        fields = ('title','class_name', 'text','duration','start_time','address')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs = {'class':'form-control'}),
            'duration':forms.TextInput(attrs={'class':'form-control','placeholder':'eg: 2 hours'}),
            'start_time':forms.DateTimeInput(format=('%m/%d/%y %H:%M'), attrs = {'class':'form-control','placeholder':'10/25/06 14:30'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'eg: clark, rice, discord..'}),
            }


class StudySessionEditForm(ModelForm):
    class Meta:
        model = StudySessionModel
        fields = ('title', 'text','duration','start_time','address')
        #start_time = forms.DateTimeField(input_formats = ['%Y-%m-%d %H:%M'], widget=forms.DateTimeInput(attrs={'class':'form-control form-control-lg','type':'datetime-local'}))
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs = {'class':'form-control'}),
            'duration':forms.TextInput(attrs={'class':'form-control','placeholder':'eg: 2 hours'}),
            'start_time':forms.DateTimeInput(format=('%m/%d/%y %H:%M'), attrs = {'class':'form-control','placeholder':'10/25/06 14:30'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'eg: clark, rice, discord..'}),
            
            }


class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['description_field', 'subject_field', 'course_number_field', 'instructor_field']
