from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import User
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def profile(request, username):
    user = User.objects.get(username=username)
    context = {'user': user}
    return render(request, 'accounts/profile.html', context)

def user_settings(request):
  if request.user.is_authenticated:
    if request.method == 'GET':
      user = request.user
      context = { 'user': user }
      return render(request, 'accounts/user_settings.html', context)
    elif request.method == 'POST':
      nickname = request.POST.get('nickname', '')
      text = request.POST.get('text', '')
      user = request.user
      user.nickname, user.text = nickname, text
      user.save()
      return HttpResponseRedirect('/')
  else:
    return HttpResponse('Unauthorized', status=401)
