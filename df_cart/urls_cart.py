from django.urls import path
from . import views


app_name = 'df_cart'
urlpatterns = [
    path('', views.cart, name='cart'),
    path('<int:goods_id>/<int:count>/', views.add, name='add'),
    path('edit/<int:cart_id>/<int:count>/', views.count_edit, name='count_edit'),
    path('delete/<int:cart_id>/', views.delete, name='del'),
]
