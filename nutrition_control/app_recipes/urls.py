from .views import *
from django.urls import path

urlpatterns = [
    path('create_product', CreateProduct.as_view(), name='create_prod'),
    path('product_list', ProductListView.as_view(), name='prod_list'),
    path('<int:pk>', ProductDetailView.as_view(), name='prod_detail')
]
