from django.urls import path, include
from . import views

urlpatterns = [
    path('api/cats/random/<int:count>/', views.random_cat_image, name='random_cat_image'),
    path('api/cats/random/', views.random_cat_image),
    path('', views.index, name='index'),
]