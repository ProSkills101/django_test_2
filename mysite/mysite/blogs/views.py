from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Blog
from files.models import File

# Create your views here.
def index(request):
  #blogs = Blog.objects.filter(state='open').order_by('-created')
  blogs = Blog.objects.order_by('-created')
  context = {'blogs': blogs}
  return render(request, 'blogs/index.html', context)

def blog(request, blog_id):
  blog = Blog.objects.get(pk=blog_id)
  if not blog:
    return HttpResponse("blog does not exist", status=404)

  context = {'blog': blog}
  return render(request, 'blogs/blog.html', context)

def myblogs(request):
  if request.user.is_authenticated:
    blogs = Blog.objects.filter(user=request.user).order_by('-created')
    context = {'blogs': blogs}
    return render(request, 'blogs/myblogs.html', context)

  return HttpResponse('Unauthorized', status=401)

def myblog(request, blog_id):
  if request.user.is_authenticated:
    blog = Blog.objects.get(pk=blog_id)
    if not blog:
      return HttpResponse("blog does not exist", status=404)

    files = File.objects.filter(user=request.user).order_by('-created')
    context = {'blog': blog, 'files': files}
    return render(request, 'blogs/myblog.html', context)

  return HttpResponse('Unauthorized', status=401)

def _validate_blog(blog):
  errors = {}
  if not blog.get('title'):
    errors['title'] = { 'msg': 'Title can not be blank.' }
  if not blog.get('html'):
    errors['html'] = { 'msg': 'Title can not be blank.' }
  return errors

def myblogs_create(request):
  if request.user.is_authenticated:
    if request.method == 'GET':
      files = File.objects.filter(user=request.user).order_by('-created')
      return render(request, 'blogs/myblogs-create.html', { 'files': files })
    elif request.method == 'POST':
      title = request.POST.get('title')
      html = request.POST.get('html')
      cover = request.POST.get('cover')

      errors = _validate_blog({'title': title, 'html': html})
      if errors:
        return JsonResponse({ 'errors': errors })
      
      blog = Blog(user=request.user, title=title, html=html, cover=cover)
      blog.save()
      
      return JsonResponse({ 'status': 200, 'msg': 'success', 'blog_id': blog.id })

  return JsonResponse({ 'status': 401, msg: 'unauthorized' })

def myblogs_update(request, blog_id):
  if request.user.is_authenticated:
    blog = Blog.objects.get(pk=blog_id)
    if not blog:
      return HttpResponse("blog does not exist", status=404)
      
    if request.method == 'POST':
      title = request.POST.get('title')
      html = request.POST.get('html')
      cover = request.POST.get('cover')

      errors = _validate_blog({'title': title, 'html': html})
      if errors:
        return JsonResponse({ 'errors': errors })
      
      blog.title = title
      blog.html = html
      blog.cover = cover
      blog.updated = timezone.now()
      blog.save()
 
      return JsonResponse({ 'status': 200, 'msg': 'success', 'blog_id': blog.id  })
  
  return JsonResponse({ 'status': 401, msg: 'unauthorized' })

@csrf_exempt
def myblogs_delete(request, blog_id):
  if request.user.is_authenticated:
    if request.method == 'DELETE':
      blog = Blog.objects.get(pk=blog_id)
      if not blog:
        return JsonResponse({ 'status': 404, 'msg': 'not found'})
      
      blog.delete()
      return JsonResponse({ 'status': 200, 'msg': 'success'})
  
  return JsonResponse({ 'status': '401', 'msg': 'unauthorized'})