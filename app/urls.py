from django.urls import path, include
from django.contrib import admin
from . import views
from django.views.generic import TemplateView
from .views import StudySessionDetailView,AddSessionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"),name = "home"),
    path("", include("allauth.urls")),
    path('class/', views.get_class,name = "get_class"),
    path('search/', views.get_search,name = "search"),
    path('study_session_post', AddSessionView.as_view(),name = "post"),
    path('list/', views.post_list,name = 'list'),
    path('list/<int:pk>', StudySessionDetailView.as_view(), name = "post_detail"),
    path('user_list/', views.user_list,name = 'userList'),
    path('userSearch/', views.get_user_search,name = "userSearch"),

]
