from django.db import models
from django.conf import settings

from products.models import Product
from django.db.models.signals import pre_save, m2m_changed

# Create your models here.
User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user            = models.ForeignKey(User, null=True, blank=True)
    products        = models.ManyToManyField(Product,blank=True)
    subtotal        = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total           = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

def cart_m2m_changed_receiver(sender, action, instance, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for x in products:
            total += x.price
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()

m2m_changed.connect(cart_m2m_changed_receiver, sender=Cart.products.through)

def cart_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = instance.subtotal + 10 #* 1.08
    else:
        instance.total = 0.00

pre_save.connect(cart_pre_save_receiver,sender=Cart)