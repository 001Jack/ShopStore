import time

from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from User.models import PayOrder, Address, BuyCar, PayInfo
from store import models
from User import models as user_model
from .AliPay import aliPay

from User.views import setpassword


# Create your views here.
# 注册
def register(request):
    return render(request, 'shoppingcart/register.html')


# 登录
def login(request):
    return render(request, 'shoppingcart/login.html')


# 首页
def index(request):
    type_list = models.GoodsType.objects.all()
    return render(request, 'shoppingcart/index.html', locals())


def detail(request):
    ids = request.GET.get('id', 1)
    goods = models.Goods.objects.filter(id=int(ids)).first()
    return render(request, 'shoppingcart/detail.html', locals())


def goods_list(request):
    id = request.GET.get('id')
    keywords = request.GET.get('keywords')
    page = request.GET.get('page', 1)
    # 获取商品部分
    goods_list = models.Goods.objects.filter(status=1)
    if id:
        goods_type = models.GoodsType.objects.filter(id=id).first()
        if goods_type:
            goods_list = goods_type.goods_set.filter(status=1)
    if keywords:
        goods_list = models.Goods.objects.filter(name__contains=keywords, status=1)
    # 分页
    paginator = Paginator(goods_list, 10)
    page_data = paginator.page(int(page))

    return render(request, 'shoppingcart/list.html', locals())


def user_address(request):
    user_id = request.GET.get(id)
    user = user_model.User.objects.get(id=1)
    # 获取 用户的所有地址
    address_list = user.address_set.all()
    now_address = user.address_set.filter(is_now=1).first()

    # 请求保存
    if request.method == "POST":
        recver = request.POST.get("recver")
        address = request.POST.get("address")
        post_code = request.POST.get("post_code")
        phone = request.POST.get("phone")

        addr = user_model.Address()
        addr.recipients = recver
        addr.address = address
        addr.post_code = post_code
        addr.phone = phone
        addr.user = user_model.User.objects.get(id=1)
        addr.save()
    return render(request, 'shoppingcart/user_center_site.html', locals())


def setDefaultAddress(request):
    user_id = request.COOKIES.get("user_id")  # 拥有登录才会有效

    address_id = int(request.GET.get("id"))  # 获取将要被设为默认地址的地址

    user = user_model.User.objects.get(id=1)  # 获取用户
    address_list = user.address_set.all()  # 获取用户所有地址
    address_list.update(is_now=0)  # 讲默认去除

    address = user_model.Address.objects.get(id=address_id)  # 设置新的默认
    address.is_now = 1
    address.save()
    return redirect('/shop/address/')


def add_shop_car(request):
    user_id = request.COOKIES.get('user_id')

    user = user_model.User.objects.get(id=1)
    goods_number = request.POST.get('goods_number')
    goods_id = request.POST.get('goods_id')
    goods = models.Goods.objects.get(id=int(goods_id))

    by = user_model.BuyCar()
    by.goods_name = goods.name
    by.goods_price = goods.price
    by.goods_total = goods.price * int(goods_number)
    by.goods_number = int(goods_number)
    by.goods_picture = goods.picture
    by.goods_store = goods.store
    by.user = user
    by.save()

    return JsonResponse({'data': '保存成功！'})


# 商品购物车
def shop_car(request):
    user_id = request.COOKIES.get("user_id")
    user = user_model.User.objects.get(id=1)
    goods_list = user.buycar_set.all()
    return render(request, 'shoppingcart/cart.html', locals())


# 商品订单
def place_order(request):
    user_id = request.COOKIES.get("user_id")  # 登录状态下设置的cookie
    user = user_model.User.objects.get(id=1)
    address = user.address_set.filter(is_now=1).first()

    if request.method == 'POST':
        post_data = request.POST.get("cart_goods")
        goods_id = request.POST.getlist("cart_goods")
        goods_list = [user_model.BuyCar.objects.get(id=int(i)) for i in goods_id]
    return render(request, 'shoppingcart/place_order.html', locals())


def save_order(request):
    user_id = request.COOKIES.get("user_id")  # 拥有登录才会有效
    user = user_model.User.objects.get(id=1)
    if request.method == "POST":
        address_id = request.POST.get("addr_id")
        cart_id = request.POST.getlist("car_id")
        time_str = str(time.time()).replace(".", address_id)

        # 保存订单总表
        pay_order = PayOrder()
        pay_order.pay_number = time_str
        pay_order.pay_status = 1
        pay_order.goods_total = len(cart_id) - 1
        pay_order.user = user
        pay_order.address = Address.objects.get(id=int(address_id))
        pay_order.save()
        # 保存订单详情表
        pay_total = 0
        for id in cart_id:
            if id.isdigit():
                cart_goods = BuyCar.objects.get(id=int(id))
                pay_info = PayInfo()
                pay_info.goods_name = cart_goods.goods_name
                pay_info.goods_price = cart_goods.goods_price
                pay_info.goods_number = cart_goods.goods_number
                pay_info.goods_total = cart_goods.goods_total
                pay_info.goods_picture = cart_goods.goods_picture
                pay_info.goods_store = cart_goods.goods_store
                pay_info.pay_status = 1
                pay_info.order_id = pay_order
                pay_info.save()

                pay_total += cart_goods.goods_total

                # 保存订单总价
                pay_order.pay_price = pay_total
                pay_order.save()

        pay_url = aliPay(pay_order.pay_number, pay_total)
        result = {"state": "success", "pay_url": pay_url}
    else:
        result = {"state": "error", "pay_url": ""}
    return JsonResponse(result)


from CeleryTask.tasks import add, sendDing


def get_celery(request):
    for i in range(1, 100):
        add.delay(i, i)
    return HttpResponse('调用完成！')


# 忘记密码
def forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = user_model.User.objects.filter(email=email).first()
        send_message = """
            demo测试：
            请点击下方链接找回密码：%s
        """
        if user:
            token = str(time.time()) + email
            token = setpassword(token)
            content = 'http://127.0.0.1:8000/shop/cp/?token=%s&email=%s' % (token, email)
            sendDing.delay(send_message % content)
            change = user_model.Cpassword.objects.filter(email=email).first()
            if not change:
                change = user_model.Cpassword()
                change.email = email
            change.token = token
            change.is_chage = 0
            change.save()
    return render(request, 'shoppingcart/forget_password.html', locals())


# 修改密码
def change_password(request):
    if request.method == 'POST':
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        token = request.POST.get('token')
        user = user_model.Cpassword.objects.filter(email=email).first()
        if user and user.is_chage == 0:
            if token == user.token:
                user = user_model.User.objects.get(email=email)
                user.password = setpassword(password)
                user.save()
            else:
                "token 错误"
    else:
        "用户不存在或者验证失效"
    return render(request, 'shoppingcart/change_password.html', locals())
