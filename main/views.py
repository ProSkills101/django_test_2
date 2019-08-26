from django.shortcuts import render

def index(request):
    context = {'title': 'Hello First Page'}
    return render(request, 'main/index.html', context)
# Create your views here.
