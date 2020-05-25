from django.shortcuts import render
from .models import Item, ItemVariation
from django.views.generic import ListView, DetailView, View
from django_filters.views import FilterView
from math import ceil
from . filters import ItemFilter
from django.core.paginator import Paginator
from . forms  import FilterForm


class homeview(ListView):

    model = Item
    template_name = 'products/home.html'
    paginate_by = 8

    def get_filter_args(self):
        request = self.request
        filter_args = {}
        filter_args['category'] = request.GET.get('category')
        filter_args['price__lte'] = request.GET.get('price')

        # To remove filter arg if the value is null. to avoid errors
        filter_args = {key: value for key, value in filter_args.items() if value}

        return filter_args

    def get_queryset(self):
        filter_args = self.get_filter_args()
        queryset = super().get_queryset().filter(**filter_args)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FilterForm()
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'products/product.html'



def search(request):
    try:
        q = request.GET.get('search')
    except:
        q = None
    if q:
        items = Item.objects.filter(title__icontains=q)
        context = {'query': q, 'items': items}
        template = 'products/results.html'
    else: 
        template = 'products/home.html'
        context = {}
    return render(request, template, context)


def about(request):
    return render(request, 'products/about.html')

def contact(request):
    return render(request, 'products/contact.html')