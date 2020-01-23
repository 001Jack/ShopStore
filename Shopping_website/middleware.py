import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class UrlMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print(request)
        # if request.method == 'GET':
        #     return HttpResponse('出门靠左！')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        pool = ['login', 'register', 'index']
        name = callback.__name__
        print(name)
        # if name not in pool:
        #     email = request.COOKIES.get("email")
        #     if email:
        #         return callback(callback_args, callback_kwargs)
        #     else:
        #         return HttpResponseRedirect('/shop/login/')

    def process_exception(self, request, exception):
        with open("error.log", "a") as f:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = "{}:{}".format(now, exception)
            f.write(result)

    def process_response(self, request, response):
        response.set_cookie("process_response", 'ok')
        return response
