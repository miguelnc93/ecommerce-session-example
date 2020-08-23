from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from django.http import Http404

from .models import *
from carts.models import *
from carts.views import *
# Create your views here.

class ProductFeatureListView(ListView):
    queryset = Product.objects.filter(featured=True, active=True)
    template_name = "products/list.html"

class ProductFeatureDetailView(DetailView):
    #Ademas de estos filter que agregue, esta clase DetailView automaticamente agrega el filter por pk
    #que se le manda por medio de la URL
    queryset = Product.objects.filter(featured=True, active=True) 
    template_name = "products/featured-detail.html"

class ProductWomenFeatureListView(ListView):
    queryset = Product.objects.filter(featured=True, active=True, categoria="MUJER")
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductWomenFeatureListView,self).get_context_data(*args,**kwargs)
        context['categoria'] = "Mujer"
        return context

class ProductMenFeatureListView(ListView):
    queryset = Product.objects.filter(featured=True, active=True, categoria="HOMBRE")
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductMenFeatureListView,self).get_context_data(*args,**kwargs)
        context['categoria'] = "Hombre"
        return context

class ProductGroceriesFeatureListView(ListView):
    queryset = Product.objects.filter(featured=True, active=True, categoria="MERCADO")
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductGroceriesFeatureListView,self).get_context_data(*args,**kwargs)
        context['categoria'] = "Mercado"
        return context

    

# class ProductListView(ListView):
#     queryset = Product.objects.all()
#     template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     print(*args)
    #     print("----->")
    #     print(**kwargs)
    #     return context
            #This context return "object_list", so if i comment this part of code
            #and use {{object_list}} directly in the template it shows the same info
            #as the method below


# def product_list_view(request):
#     queryset = Product.objects.all()
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "products/list.html",context)

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.filter(featured=True, active=True)
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args,**kwargs)
        cart_obj, new_obj = cart_new_or_get(self.request)
        context['cart'] = cart_obj
        return context



# class ProductDetailView(DetailView):
#     queryset = Product.objects.all()
#     template_name = "products/detail.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context
            #This context return "object_list", so if i comment this part of code
            #and use {{object_list}} directly in the template it shows the same info
            #as the method below


# def product_detail_view(request,pk):
#     print(pk)
#     #instance = Product.objects.get(pk=pk)
#     #instance = get_object_or_404(Product,pk=pk)
#     try:
#         instance = Product.objects.get(id=pk)
#     except Product.DoesNotExist:
#         raise Http404("Product doesnt exist")
#     context = {
#         "object": instance
#     }
#     return render(request, "products/detail.html",context)
