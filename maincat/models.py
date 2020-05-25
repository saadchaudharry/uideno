from django.db import models
from django.db.models.signals import pre_save
from uideno.utils import unique_slug_generator


# Create your models here.


class Catagory(models.Model):
    title =models.CharField(max_length=100)
    img   =models.ImageField(upload_to='catagory_img')
    slug    =models.SlugField(max_length=100,blank=True,null=True)

    def __str__(self):
        return str(self.title)

def cata_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(cata_slug,sender=Catagory)



class Prod(models.Model):
    title   =models.CharField(max_length=100)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    href    =models.CharField(max_length=100)
    img     =models.ImageField(upload_to='prod_img')
    publish =models.BooleanField(default=1)
    slug    =models.SlugField(max_length=100,blank=True,null=True)

    def __str__(self):
        return str(self.title)

def prod_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(prod_slug,sender=Prod)