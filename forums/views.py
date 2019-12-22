from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone

from .models import Forum, Topic, Post, Comment

# Create your views here.

def index(request):
  forums = Forum.objects.order_by('-created')
  context = {'forums': forums}
  return render(request, 'forums/index.html', context)

def forum(request, forum_id):
  forum = Forum.objects.get(pk=forum_id)
  topics = Topic.objects.filter(forum=forum).order_by('-created')
  return render(request, 'forums/forum.html', {'forum': forum, 'topics': topics })

def topic(request, forum_id, topic_id):
  forum = Forum.objects.get(pk=forum_id)
  topic = Topic.objects.get(pk=topic_id)
  posts = Post.objects.filter(topic=topic)
  return render(request, 'forums/topic.html', {'forum': forum, 'topic': topic, 'posts': posts })

def _validate_topic(topic):
  errors = {}
  if not topic.get('title'):
    errors['title'] = { 'msg': 'Title can not be blank.' }
  if not topic.get('html'):
    errors['html'] = { 'msg': 'Html can not be blank.' }
  return errors

def topic_create(request, forum_id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      title = request.POST.get('title')
      html = request.POST.get('html')

      errors = _validate_topic({ 'title': title, 'html': html })
      if errors:
        return JsonResponse({ 'errors': errors })
      
      forum = Forum.objects.get(pk=forum_id)
      topic = Topic(user=request.user, forum=forum, title=title, html=html)
      topic.save()
      
      return JsonResponse({ 'status': 200, 'msg': 'success', 'topic_id': topic.id })

  return JsonResponse({ 'status': 401, msg: 'unauthorized' })

def topic_update(request, forum_id, topic_id):
  if request.user.is_authenticated:
    topic = Topic.objects.get(pk=topic_id)
    if not topic:
      return JsonResponse({ 'status': 404, msg: 'not found' })
      
    if request.method == 'POST':
      title = request.POST.get('title')
      html = request.POST.get('html')

      errors = _validate_topic({'title': title, 'html': html})
      if errors:
        return JsonResponse({ 'errors': errors })
      
      topic.title = title
      topic.html = html
      topic.updated = timezone.now()
      topic.save()
 
      return JsonResponse({ 'status': 200, 'msg': 'success', 'topic_id': topic.id  })
  
  return JsonResponse({ 'status': 401, msg: 'unauthorized' })

def _validate_post(post):
  errors = {}
  if not post.get('html'):
    errors['html'] = { 'msg': 'Html can not be blank.' }
  return errors

def post_create(request, forum_id, topic_id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      html = request.POST.get('html')

      errors = _validate_post({ 'html': html })
      if errors:
        return JsonResponse({ 'errors': errors })
      
      topic = Topic.objects.get(pk=topic_id)
      post = Post(user=request.user, topic=topic, html=html)
      post.save()
      
      return JsonResponse({ 'status': 200, 'msg': 'success', 'post_id': post.id })

  return JsonResponse({ 'status': 401, msg: 'unauthorized' })

def post_update(request, forum_id, topic_id, post_id):
  if request.user.is_authenticated:
    post = Post.objects.get(pk=post_id)
    if not topic:
      return JsonResponse({ 'status': 404, msg: 'not found' })
      
    if request.method == 'POST':
      html = request.POST.get('html')

      errors = _validate_post({'html': html})
      if errors:
        return JsonResponse({ 'errors': errors })
      
      post.html = html
      post.updated = timezone.now()
      post.save()
 
      return JsonResponse({ 'status': 200, 'msg': 'success', 'post_id': post.id  })
  
  return JsonResponse({ 'status': 401, msg: 'unauthorized' })

def _validate_comment(comment):
  errors = {}
  if not comment.get('text'):
    errors['text'] = { 'msg': 'Text can not be blank.' }
  return errors

def comment_create(request, forum_id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      topic_id = request.POST.get('topic_id')
      post_id = request.POST.get('post_id')
      html = request.POST.get('html')

      errors = _validate_post({ 'html': html })
      if errors:
        return JsonResponse({ 'errors': errors })
      
      if topic_id:
        topic = Topic.objects.get(pk=topic_id)
      if post_id:
        post = Post.objects.get(pk=post_id)

      comment = Comment(user=request.user, topic=topic, post=post, text=text)
      comment.save()
      
      return JsonResponse({ 'status': 200, 'msg': 'success', 'comment_id': comment.id })

  return JsonResponse({ 'status': 401, msg: 'unauthorized' })

def comment_update(request, forum_id, comment_id):
  if request.user.is_authenticated:
    comment = Comment.objects.get(pk=comment_id)
    if not comment:
      return JsonResponse({ 'status': 404, msg: 'not found' })
      
    if request.method == 'POST':
      text = request.POST.get('text')

      errors = _validate_topic({'text': text})
      if errors:
        return JsonResponse({ 'errors': errors })
      
      comment.text = text
      comment.updated = timezone.now()
      comment.save()
 
      return JsonResponse({ 'status': 200, 'msg': 'success', 'post_id': post.id  })
  
  return JsonResponse({ 'status': 401, msg: 'unauthorized' })
