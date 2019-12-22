from django.urls import path

from . import views

app_name = 'files'
urlpatterns = [
  path('', views.index, name='index'),
  path('fileupload', views.fileupload, name='fileupload'),
]