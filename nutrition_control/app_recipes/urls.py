from .views import *
from django.urls import path


urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('product_list', ProductListView.as_view(), name='prod_list'),
    path('product_list/<int:pk>', ProductDetailView.as_view(), name='prod_detail'),
    path('create_product', CreateProductView.as_view(), name='create_prod'),
]

