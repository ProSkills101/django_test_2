from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import User
from .forms import UserSettingForm

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
def user_settings(request):
    if request.user.is_authenticated:
      if request.method == 'GET':
        form = UserSettingForm()
        user = request.user
        context = { 'user': user, 'form': form }
        return render(request, 'accounts/user_settings.html', context)
      elif request.method == 'POST':
        form = UserSettingForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
          context = { 'user': request.user, 'form': form }
          return render(request, 'accounts/user_settings.html', context)
    else:
      return HttpResponse('Unauthorized', status=401)
    
def profile(request, username):
    user = User.objects.get(username=username)
    context = { 'user': user }
    return render(request, 'accounts/profile.html', context)