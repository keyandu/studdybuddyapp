from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


#
# # Create your models here.
class UserClass(models.Model):
    description_field = models.CharField(max_length=50, default="description")
    course_number_field = models.CharField(max_length=10, default="course number")
    instructor_field = models.CharField(max_length=50, default="instructor")
    def __str__(self):
        return self.description_field


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Age = models.TextField()
    Enrolled_Courses = models.TextField()
    Major = models.TextField()
    Bio = models.TextField()
    def __str__(self):
        return f'{self.user.username} Profile'


