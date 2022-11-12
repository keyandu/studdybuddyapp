from django.contrib import admin
from django.urls import include, path
from app.views import edit_profile, profile, add_class





urlpatterns = [
    path('', include('app.urls')),
    path('app/', include('app.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('<int:pk>/profile/', profile.as_view(), name='user_profile'),
    #path('friends/', friendslist, name='edit_profile_page'),
    path('<int:pk>/profile/edit/', edit_profile, name='edit_profile_page'),
    path('class/addclass/', add_class, name='add_class'),
]
