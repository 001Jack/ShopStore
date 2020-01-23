from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from . import models
import hashlib


# Create your views here.
# md5 加密
def setpassword(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode())
    result = md5.hexdigest()
    return result


def register(request):
    """
    用户注册逻辑处理
    :param request:
    :return:
    """
    before_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        username = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        redirect = request.POST.get('redirect')

        # 创建一个空对象
        user = models.User()
        user.username = username
        user.password = setpassword(pwd)
        user.email = email
        user.save()
        return HttpResponseRedirect('/shop/login/')

    return HttpResponseRedirect(before_url)


def login(request):
    last_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        next_url = request.POST.get('redirect')

        user = models.User.objects.filter(username=username).first()

        if user:
            if user.password == setpassword(pwd):
                return HttpResponseRedirect(next_url)
            return HttpResponseRedirect(last_url)
        return HttpResponseRedirect(last_url)
