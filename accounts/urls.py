from django.urls import path

from . import views

urlpatterns = [
  path('signup/', views.SignUp.as_view(), name='signup'),
  path('user_settings/', views.user_settings, name='user_settings'),
]