from allauth.account.forms import SignupForm
from django.forms import ModelForm
from .models import Profile, StudySessionModel
from django import forms

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
        #start_time = forms.DateTimeField(input_formats = ['%Y-%m-%d %H:%M'], widget=forms.DateTimeInput(attrs={'class':'form-control form-control-lg','type':'datetime-local'}))
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'class_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'eg: CS 1110'}),
            'text': forms.Textarea(attrs = {'class':'form-control'}),
            'duration':forms.TextInput(attrs={'class':'form-control','placeholder':'eg: 2 hours'}),
            'start_time':forms.Select(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'eg: clark, rice, discord..'}),
            
            }
