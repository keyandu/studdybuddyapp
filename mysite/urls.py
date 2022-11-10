from django.contrib import admin
from django.urls import include, path
from app.views import edit_profile, profile, friendslist





urlpatterns = [
    path('', include('app.urls')),
    path('app/', include('app.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('<int:pk>/profile/', profile.as_view(), name='user_profile'),
    path('friends/', friendslist, name='edit_profile_page'),
    path('<int:pk>/profile/edit/', edit_profile, name='edit_profile_page')]
