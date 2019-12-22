from django.shortcuts import render
from .models import Carousel, Notice


    


def index(request):
    carousels = Carousel.objects.order_by('-pub_date')[:5]
    notices = Notice.objects.order_by('-pub_date')[:5]
    context = {'carousels': carousels, 'notices': notices}
    return render(request, 'main/index.html', context)
# Create your views here.
