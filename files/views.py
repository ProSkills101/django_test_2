from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .models import File

# Create your views here.
def index(request):
  if request.user.is_authenticated:
    files = File.objects.order_by('-created')
    context = {'files': files}
    return render(request, 'files/index.html', context)
  
  return HttpResponse('Unauthorized', status=401)

def fileupload(request):
  if request.user.is_authenticated:
    if request.method == 'POST':  
      desc = request.POST.get('desc', '')
      tag = request.POST.get('tag', '')
      file = request.FILES.get('file')
      name = str(file)

      if not file:
        return JsonResponse({ 'status': 400, 'msg': 'not found' })

      #for f in request.FILES.getlist('file'):
      #  name = str(f)
      #print(desc, tag, type(file))

      file = File(user=request.user, name=name, desc=desc, file=file, tag=tag)
      file.save()
      return JsonResponse({ 'status': 200, 'msg': 'ok' })
      
  return JsonResponse({ 'status': 401, 'msg': 'Unauthorized' })
