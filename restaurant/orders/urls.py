from django.urls import path

from orders import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('order', views.place_order,name='place_order'),
    path('order/success', views.order_success,name='order_success'),
]