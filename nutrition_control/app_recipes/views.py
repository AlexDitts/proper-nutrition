from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from .forms import ProductForm, ExcludeProductsForm
from .models.models import Product, Recipe


class MainPageView(generic.TemplateView):
    template_name = 'app_recipes/main_page.html'


class ProductListView(generic.ListView):
    model = Product
    template_name = 'app_recipes/list_of_product.html'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'app_recipes/detail_product.html'


class CreateProductView(generic.CreateView):
    template_name = 'app_recipes/form.html'
    model = Product
    form_class = ProductForm
    success_url = 'product_list'


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'app_recipes/list_of_recipes.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        form_prod = ExcludeProductsForm()
        context['prod_list'] = Product.objects.all()
        context['form'] = form_prod
        return context

    def get_queryset(self):
        get_params = list(map(int, self.request.GET.getlist('title')))
        queryset = Recipe.objects.exclude_products(products=get_params)
        return queryset


class TestView(generic.TemplateView):
    template_name = 'app_recipes/recipe_card.html'
