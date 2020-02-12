from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  get_user_model
from django.urls import reverse_lazy
from django.views import generic
from django import forms
#from .models import User

User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class SignUp(generic.CreateView):
    form_class = SignUpForm
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
