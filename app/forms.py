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
        fields = ('title','author', 'text','duration','start_time','address')
        #start_time = forms.DateTimeField(input_formats = ['%Y-%m-%d %H:%M'], widget=forms.DateTimeInput(attrs={'class':'form-control form-control-lg','type':'datetime-local'}))
        widgets={
            'text': forms.Textarea(attrs = {'cols': 80, 'rows': 20})
            }
