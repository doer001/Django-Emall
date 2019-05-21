# coding:utf-8
from django.http import HttpResponseRedirect


# 如果未登录则转到登录页面
def login(func):
    def login_fun(request, *args, **kwargs):
        if 'user_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_fun

# request.path 表示当前路径
# request.get_full_path() 表示完整路径，包含get参数
