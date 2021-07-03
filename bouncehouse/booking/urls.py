from django.urls import path, include
from . import views


urlpatterns = [
    path('',
         views.ProductList.as_view()),
    path('<slug:category_slug>/<slug:product_slug>/',
         views.ProductDetail.as_view()),
    path('<slug:category_slug>/', views.ProductByCollection.as_view()),
]
