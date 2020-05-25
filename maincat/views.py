from django.shortcuts import render,get_object_or_404,HttpResponse
from django.views.generic import ListView
from .models import Catagory,Prod
# Create your views here.


class cata(ListView):
    model = Catagory
    template_name = 'index.html'

def product(request,catagory_slug):
    products=Prod.objects.filter(publish=1)
    if catagory_slug:
        catagory =get_object_or_404(Catagory,slug=catagory_slug)
        products =products.filter(catagory=catagory)
    context={'prod':products}
    return render(request , 'detail.html' ,context)