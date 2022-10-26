from django.contrib import admin
from django.urls import include, path
from app.views import profile
from app.views import EditProfilePageView




urlpatterns = [
    path('', include('app.urls')),
    path('app/', include('app.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('<int:pk>/profile/', profile.as_view(), name='user_profile'),
    path('<int:pk>/profile/edit/', EditProfilePageView.as_view(), name='edit_profile_page')]
