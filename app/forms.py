from django.forms import ModelForm
from .models import Profile

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['Age', 'Major', 'Enrolled_Courses', 'Bio']

