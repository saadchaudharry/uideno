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

def search(request):

    if request.method =="GET":
        obj1 = request.GET.get('searchtype')
        cat_bd =Catagory.objects.filter(title__contains=obj1)
        prod_bd=Prod.objects.filter(title__contains=obj1)
    context={'catagory':cat_bd,'product':prod_bd}
    return render(request, 'search.html',context)
