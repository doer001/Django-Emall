from django.urls import path
from . import views

app_name = 'df_goods'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/<int:type_id>/<int:page_id>/<int:sort_id>/', views.good_list, name='goods_list'),
    path('detail/<int:goods_id>/', views.goods_detail, name='good_detail'),
    path('search/', views.MySearchView(), name='haystack_search'),  # views.MySearchView()，括号必带
]
