from django.urls import path

from . import views

app_name = 'forums'
urlpatterns = [
  path('', views.index, name='index'),
  path('forum/<int:forum_id>/', views.forum, name='forum'),
  path('forum/<int:forum_id>/topic/<int:topic_id>/', views.topic, name='topic'),
  path('forum/<int:forum_id>/topic/create/', views.topic_create, name='topic-create'),
  path('forum/<int:forum_id>/topic/<int:topic_id>/update/', views.topic_update, name='topic-update'),
  path('forum/<int:forum_id>/topic/<int:topic_id>/post/create/', views.post_create, name='post-create'),
  path('forum/<int:forum_id>/topic/<int:topic_id>/post/<int:post_id>/update/', views.post_update, name='post-update'),
  path('forum/<int:forum_id>/comment/create/', views.comment_create, name='comment-create'),
  path('forum/<int:forum_id>/comment/<int:comment_id>/update/', views.comment_update, name='comment-update'),
  
]