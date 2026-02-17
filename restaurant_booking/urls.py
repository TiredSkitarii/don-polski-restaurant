from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.create_booking, name='create_booking'),
    path('change/<int:pk>/', views.change_booking, name='change_booking'),
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),
    path('list/', views.booking_list, name='booking_list')
]
