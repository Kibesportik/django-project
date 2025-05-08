from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('new-order/<int:product_id>/',views.CreateOrder.as_view(), name='new-order'),
    path('product-search/',views.product_search, name='product_search'),
]
