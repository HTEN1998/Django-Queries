from django.urls import path
from . import views

urlpatterns=[
    path('orders',views.orders_view,name="index"),
    path('orders_view',views.orders_view,name="orders_view")
]