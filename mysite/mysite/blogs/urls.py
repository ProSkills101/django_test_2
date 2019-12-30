from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:blog_id>/', views.blog, name='blog'),
  path('myblogs', views.myblogs, name='myblogs'),
  path('myblogs/<int:blog_id>/', views.myblog, name='myblog'),
  path('myblogs/create/', views.myblogs_create, name='myblogs-create'),
  path('myblogs/update/<int:blog_id>/', views.myblogs_update, name='myblogs-update'),
  path('myblogs/delete/<int:blog_id>/', views.myblogs_delete, name='myblogs-delete'),
]