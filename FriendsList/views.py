from django.shortcuts import render

# Create your views here.
class friendslist(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'friendsList.html', context)