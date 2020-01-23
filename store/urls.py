from django.urls import path, re_path

from store import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'store'

urlpatterns = [
    path('store_index/', views.store_index, name='store_index'),  # 后台首页
    path('store_list/', views.store_list, name='store_list'),  # 商品详情
    path('store_add/', views.store_add, name='store_add'),  # 商品详情
    path('ajax_store_add/', views.ajax_store_add, name='ajax_store_add'),  # ajax 添加商品
    path('change_button_down/', views.change_button_down, name='change_button_down'),  # ajax 添加商品
    path('goodsView/', views.GoodsView.as_view(), name='GoodsView'),  # 视图类
    path('list_vue/', views.list_vue, name='list_vue'),  # vue商品信息页面
    re_path(r'^list_vue/(?P<id>\d+)/$', views.product_details, name='product_details'),  # 商品详细信息页面
    re_path(r'^store_update/(?P<id>\d+)/$', views.store_update, name='store_update'),  # 商品信息修改
    re_path(r'^payresult/$', views.payresult),
    re_path(r'^pay/$', views.pay),
    path('getData/', views.getData, name='getData'),  # 添加购物车
]
