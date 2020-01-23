from django.urls import path, re_path
from shopping_cart import views

app_name = 'shop'
urlpatterns = [
    path('register/', views.register, name='register'),  # 注册页面的显示
    path('login/', views.login, name='login'),  # 登录页面的显示
    re_path(r'^index/$', views.index, name='index'),  # 登录页面的显示
    path('detail/', views.detail, name='detail'),  # 用户详情的显示
    path('goods_list/', views.goods_list, name='goods_list'),  # 商品类型的显示
    path('address/', views.user_address, name='user_address'),
    path('address_add/', views.setDefaultAddress, name='address_add'),  # 地址添加
    path('add_shop_car/', views.add_shop_car, name='add_shop_car'),  # 添加购物车
    path('cart/', views.shop_car, name='shop_car'),  # 商品购物车页面
    path('place_order/', views.place_order, name='place_order'),  # 订单
    path('save_order/', views.save_order, name='save_order'),  # 保存订单
    path('sa/', views.get_celery, name='get_celery'),  # celery的测试
    path('fw/', views.forget_password, name='forget_password'),  # 忘记密码
    path('cp/', views.change_password, name='change_password'),  # 修改密码
]
