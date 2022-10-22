from django.contrib import admin
from django.urls import include, path
from app.views import profile

urlpatterns = [
    # Add this

]
urlpatterns = [
    path('', include('app.urls')),
    path('app/', include('app.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('profile/', profile, name='users-profile'),
]
