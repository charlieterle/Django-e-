from django.urls import path
from django.urls import re_path

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^book/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product_detail'),
]