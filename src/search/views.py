from django.shortcuts import render
from products.models import *
from django.db.models import Q
from django.views.generic import *
import re

# Create your views here.
class SearchProductListView(ListView):
    #queryset = Product.objects.all()
    template_name = "search/view.html"

    #If i want to include search on the project
    def get_queryset(self,*args,**kwargs):
        request = self.request
        print(request.GET) #method_dictionary
        query = request.GET.get('q') #adding the ".get('q') instead of using only request.GET['q'] 
                                     #it handles the error of key not found in dictionary
                                     #and also you can add a default search value
                                     #.get('q', 'totoro')
        if query is not None:
            #add my own filter
            #trim, lower, remove special caracters, join text, and search
            #option 2: add another field to model(Product) hidden. That contains the title name but 
            #with the filters below
            print(re.sub('\W','',query.replace(" ","")))
            lookups_or = (
                            Q(title__icontains=re.sub('\W','',query.replace(" ",""))) | 
                            Q(description__icontains=re.sub('\W','',query.replace(" ",""))) |
                            Q(price__icontains=query.replace(" ","")) | 
                            Q(tag__title__icontains=re.sub('\W','',query.replace(" ","")))
                        )
            lookups_and = (
                            Q(featured=True) & 
                            Q(active=True)
                        )
            return Product.objects.filter(lookups_or, lookups_and).distinct()
        else:
            return Product.objects.filter(featured=True, active=True)
