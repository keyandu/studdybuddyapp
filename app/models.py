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
    Ages = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Age = models.CharField(max_length=150, choices=Ages)
    Enrolled_Courses = models.TextField()
    Major = models.TextField()
    Bio = models.TextField()
    def __str__(self):
        return f'{self.user.username} Profile'

    class UserInfo(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)

        class_subject = models.CharField(max_length=10)
        class_number = models.CharField(max_length=10)
        class_section = models.CharField(max_length=10)


