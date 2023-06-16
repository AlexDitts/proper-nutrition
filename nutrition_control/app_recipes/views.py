from django.views import generic
from .forms import ProductForm
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


class TestView(generic.TemplateView):
    template_name = 'app_recipes/recipe_card.html'
