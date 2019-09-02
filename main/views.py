from django.shortcuts import render
from .models import Carousel


    


def index(request):
    carousels = Carousel.objects.order_by('-pub_date')[:5]
    context = {'carousels': carousels}
    print("XXXXXXXXXX",context)
    return render(request, 'main/index.html', context)
# Create your views here.
