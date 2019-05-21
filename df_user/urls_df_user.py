from django.urls import path
from . import views

app_name = 'df_user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_handle/', views.register_handle, name='register_handle'),
    path('register_exist/', views.register_exit),
    path('login/', views.login, name='login'),
    path('login_handle/', views.login_handle, name='login_handle'),
    path('logout/', views.logout, name='logout'),
    path('info/', views.info, name='info'),
    path('order/', views.order, name='order'),
    path('site/', views.site, name='site'),
    path('order/<int:page_id>/', views.order, name='order'),
]
