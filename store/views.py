from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.views import View

from . import models


# Create your views here.


# 后台首页
def store_index(request):
    return render(request, 'store/base.html')


# 分页器
def store_list(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    # 获取前端的搜索框参数
    search = request.GET.get("search")
    print(search)

    if search:
        goods = models.Goods.objects.filter(name__contains=search).order_by('pk')
    else:
        goods = models.Goods.objects.order_by("pk")

    # 创建一个分页器
    paginator = Paginator(goods, 5)

    # 获取到指定页数的数据
    page_obj = paginator.page(page)

    return render(request, 'store/store_list_vue.html', locals())


# ajax 添加商品
def ajax_store_add(request):
    result = {'code': 400, 'data': ""}
    goods_id = request.GET.get("goods_id")
    goods_price = request.GET.get("price")

    if goods_price and goods_id:
        goods = models.Goods.objects.filter(id=goods_id).first()
        if goods:
            goods.price = goods_price
            goods.save()
            result['code'] = 200
            result['data'] = goods_price
        else:
            result['data'] = '商品不存在'
    else:
        result['data'] = '商品ID不存在或者商品不存在！'
    return JsonResponse(result)


# 改变按钮状态
def change_button_down(request):
    result = {'code': 400, 'data': ''}
    goods_id = request.GET.get('goods_id')
    goods_status = request.GET.get('status')

    goods = models.Goods.objects.filter(id=goods_id).first()

    if goods_id and goods_status:
        if goods:
            if goods_status == 'up':
                goods.status = 1
            elif goods_status == 'down':
                goods.status = 0
            goods.save()
            result['code'] = 200
            result['data'] = '修改成功'
        else:
            result['data'] = '商品不存在'
    else:
        result['data'] = '商品id不存在或未入库'
    return JsonResponse(result)


# get请求商品列表
class GoodsView(View):
    def __init__(self, **kwargs):
        super(GoodsView, self).__init__(**kwargs)
        self.result = {
            'code': '400',
            'version': 'v1',
            'data': [],
            'page_range': [],
            'page': 1,
            'page_type': [],
        }

    def get(self, request):
        # 接受url传递过来的id参数
        id = request.GET.get('id')

        if id:
            goods_list = models.Goods.objects.filter(id=id).values()
            print(goods_list)
            goods_types = models.Goods.objects.get(id=id).goods_type.type_name
            print(goods_types)
            self.result['page_type'] = goods_types
        else:
            page = request.GET.get('page')
            if page:
                page = int(page)
            else:
                page = 1
            goods_list = list(models.Goods.objects.all().values())
            # 创建分页器
            pageter = Paginator(goods_list, 3)
            goods_list = pageter.page(page).object_list
            self.result['page'] = page
            self.result['page_range'] = list(pageter.page_range)

        self.result['data'] = (list(goods_list))
        return JsonResponse(self.result, safe=False, json_dumps_params={'ensure_ascii': False})


def list_vue(request):
    return render(request, 'store/store_list_vue.html')


# 商品详情
def product_details(request, id):
    return render(request, 'store/product_details.html', locals())


# 商品修改
def store_update(request, id):
    now_store = models.Goods.objects.filter(id=id).first()
    type_list = models.GoodsType.objects.all().values()
    print(type_list)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        safe_data = request.POST.get('safe_data')
        number = request.POST.get('number')
        goods_type = request.POST.get("goods_type")
        description = request.POST.get('descript')
        picture = request.FILES.get('picture')

        # 更具传过来的id对数据进行修改
        goods = models.Goods.objects.get(id=id)

        goods.name = name
        goods.price = price
        goods.safe_date = safe_data
        goods.number = number
        goods.goods_type = models.GoodsType.objects.get(id=int(goods_type))
        goods.description = description
        if picture:
            goods.picture = picture

        goods.save()
        response = HttpResponseRedirect('/store/list_vue/')
        return response
    return render(request, 'store/store_update.html', locals())


# 商品添加
def store_add(request):
    type_list = models.GoodsType.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        safe_data = request.POST.get('safe_data')
        number = request.POST.get('number')
        description = request.POST.get('description')
        goods_type = request.POST.get("goods_type")
        picture = request.FILES.get('picture')

        goods = models.Goods()
        goods.name = name
        goods.price = pricepayresult
        goods.safe_date = safe_data
        goods.number = number
        goods.description = description
        goods.picture = picture
        goods.goods_type = models.GoodsType.objects.get(id=int(goods_type))
        goods.save()
        return HttpResponseRedirect('/store/list_vue/')

    return render(request, 'store/store_add.html', locals())


def payresult(request):
    print(request.GET)
    out_trade_no = request.GET.get('out_trade_no')
    return render(request, "store/result.html", locals())


import time
from store.alpay_obj import getUrl

def get_order():
    order = str(time.time()).replace('.', '')
    return order


def pay(request):
    params = dict(order_no=get_order(), money='10')
    url = getUrl(params)
    return HttpResponseRedirect(url)


def getData(request):
    from .spider import getSpider
    task = {
        1: "西红柿、芹菜、包菜",
        2: "鲍鱼、龙虾、甲鱼",
        3: "猪头肉、猪蹄、猪排骨",
        4: "鸡肉、土鸡蛋、鸭脖",
        5: "汤圆、饺子、海虾",
        6: "奇异果、香蕉、榴莲"
    }
    for t in task:
        for k in task[t].split("、"):
            getSpider(k,t)
    return HttpResponse("hello world")