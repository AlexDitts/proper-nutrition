from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .forms import ProductForm
from .models import Product


class CreateProduct(CreateView):

    def get(self, request):
        create_form = ProductForm()
        return render(request, 'app_recipes/form.html', context={'form': create_form})

    def post(self, request):
        create_form = ProductForm(request.POST)
        if create_form.is_valid():
            Product.objects.create(
                **create_form.cleaned_data
            )
            return render(request, 'app_recipes/success.html')


class ProductListView(ListView):
    model = Product
    template_name = 'app_recipes/list_of_product.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'app_recipes/detail_product.html'
