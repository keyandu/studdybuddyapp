from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.forms import UserChangeForm


#
# # Create your models here.
class Class(models.Model):
    description_field = models.CharField(max_length=50, default="description")
    course_number_field = models.CharField(max_length=10, default="course number")
    instructor_field = models.CharField(max_length=50, default="instructor")
    def __str__(self):
        return self.description_field, self.course_number_field, self.instructor_field


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
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()
    def __str__(self):
        return str(self.user)

Status_Choices = (('send','send'),('accepted','accepted'),)
class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=Status_Choices)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"

#class UserCourse(models.Model):
#    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#    course = models.ForeignKey(Class, on_delete=models.CASCADE)
    #user_course = UserCourse.objects.filter(user=login_user)

class StudySessionModel (models.Model):
    title = models.CharField(max_length = 200)
    text = models.CharField(max_length = 500)
    start_time = models.DateTimeField()
    duration = models.CharField(max_length = 10)
    address = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title+ ' | ' + str(self.author)



