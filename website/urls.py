from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_table, name='book_table'),
    path('menu/', views.menu, name='menu'),
]
