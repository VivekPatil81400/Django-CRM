from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:pk>', views.customer_detail, name='record'),
    path('customer_delete/<int:pk>', views.customer_delete, name='delete_record'),
    path('customer_add/', views.customer_add, name='add_record'),
]