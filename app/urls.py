from django.urls import path, include
from django.contrib import admin
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"),name = "home"),
    path("", include("allauth.urls")),
    path('class/', views.get_class,name = "get_class"),
    path('search/', views.get_search,name = "search"),
    path('finder/', TemplateView.as_view(template_name="findBuddy"), name="finder"),
    # add class path
    #path('class/classAdded', views.classAdded,name = "classAdded"),


]
