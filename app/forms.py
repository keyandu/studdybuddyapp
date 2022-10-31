from allauth.account.forms import SignupForm
from django.forms import ModelForm
from .models import Profile


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
