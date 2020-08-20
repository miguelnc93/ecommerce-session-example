from django.db import models
import random
import os
from .utils import *
from django.db.models.signals import pre_save
from django.urls import reverse

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,3999211110)
    name, ext = get_filename_ext(filename)
    final_name = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_name
        )

# class ProductManager(models.Manager):
#     def featured(self):
#         return self.get_queryset().filter(featured="False")
# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True) #pip install pillow
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
#        return "/products/{slug}/".format(slug=self.slug)
        return reverse("detail", kwargs={"slug":self.slug})


class Tag(models.Model):
    title               = models.CharField(max_length=120)
    slug                = models.SlugField()
    timestamp           = models.DateTimeField(auto_now_add=True)
    active              = models.BooleanField(default=True)
    products            = models.ManyToManyField(Product,blank=True)

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
pre_save.connect(product_pre_save_receiver, sender=Tag)
