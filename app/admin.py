from cProfile import Profile
from django.contrib import admin
from .models import Profile,StudySessionModel
# Register your models here.
admin.site.register(Profile)
admin.site.register(StudySessionModel)