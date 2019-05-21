from django.urls import path
from . import views


app_name = 'df_order'
urlpatterns = [
    path('', views.show_order, name='show_order'),
    path('push/', views.order_handle, name='push'),
    path('pay/<int:order_id>/', views.pay, name='pay'),
]
