from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from hashlib import sha1
from . import models
from . import user_decorator
from df_goods.models import GoodsInfo
from df_order.models import Order

NUM_ORDER = 2


def register(request):
    return render(request, 'df_user/register.html')


def register_handle(request):
    # 接收用户输入
    post_get = request.POST.get
    user_name = post_get('user_name')
    pwd = post_get('pwd')
    pwd2 = post_get('cpwd')
    email = post_get('email')

    # 判断两次密码
    if pwd != pwd2:
        return redirect('df_user:register')

    # 密码加密
    epwd = sha1()
    epwd.update(pwd.encode("UTF-8"))  # 参数必须为bytes类型，encode返回编码后的字符串，它是一个 bytes 对象。
    pwd = epwd.hexdigest()

    # 创建对象
    models.UserInfo.objects.create(username=user_name, password=pwd, email=email)

    # 注册成功，转到登录页面
    return redirect('df_user:login')


# 判断用户名是否已存在
def register_exit(request):
    username = request.GET.get('username')
    count = models.UserInfo.objects.filter(username=username).count()
    return JsonResponse({'count': count})


def login(request):
    username = request.COOKIES.get('username', '')  # 填错后再填可以复现
    context = {
        'username': username,
        'error_name': '0',
        'error_pwd': '0',
    }
    return render(request, 'df_user/login.html', context)


def login_handle(request):
    # 接收请求信息
    user_name = request.POST.get('user_name')
    password = request.POST.get('pwd')
    jizhu = request.POST.get('jizhu', 0)
    # 根据用户名查询对象
    users = models.UserInfo.objects.filter(username=user_name)
    if users:
        epwd = sha1()
        epwd.update(password.encode('utf8'))
        if epwd.hexdigest() == users[0].password:
            url = request.COOKIES.get('url', '/goods/index/')  # 记录之前的url，如果没有记录则设置为商品首页
            red = HttpResponseRedirect(url)  # 用变量记住,方便设置cookie
            # 记住用户名
            if jizhu:
                red.set_cookie('username', user_name)  # 设置cookie保存用户名
            else:
                red.set_cookie('username', '', max_age=-1)  # max_age指的是过期时间,当为-1时为立刻过期
            request.session['user_id'] = users[0].id  # 把用户id和名字放入session中
            request.session['user_name'] = user_name
            return red
        else:
            context = {
                'username': user_name,
                'password': password,
                'error_name': 0,
                'error_pwd': 1,
            }
            return render(request, 'df_user/login.html', context)
    else:
        context = {
            'username': user_name,
            'password': password,
            'error_name': 1,
            'error_pwd': 0,
        }
        return render(request, 'df_user/login.html', context)


@user_decorator.login
def info(request):
    user_id = request.session['user_id']
    user = models.UserInfo.objects.get(id=user_id)
    user_phone = user.phone
    user_site = user.address
    user_full_name = user.full_name
    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_ids1 = goods_ids.split(',')
    goods_list = []
    for goods_id in goods_ids1:
        if goods_id:
            goods_list.append((GoodsInfo.objects.get(id=int(goods_id))))
    context = {
        'title': '用户中心',
        'user_name': request.session['user_name'],
        'user_full_name': user_full_name,
        'user_phone': user_phone,
        'user_site': user_site,
        'goods_list': goods_list,
    }
    return render(request, 'df_user/user_center_info.html', context)


@user_decorator.login
def order(request, page_id=1):
    user_id = request.session['user_id']
    orders_list = Order.objects.filter(user_id=user_id).order_by('id')
    if orders_list:
        pages = Paginator(orders_list, NUM_ORDER)
        page = pages.page(page_id)
    else:
        pages = page = 0
    context = {
        'title': '全部订单',
        'pages': pages,
        'page': page,
    }
    return render(request, 'df_user/user_center_order.html', context)


@user_decorator.login
def site(request):
    user = models.UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post_get = request.POST.get
        user.full_name = post_get('full_name')
        user.address = post_get('address')
        user.postcode = post_get('postcode')
        user.phone = post_get('phone')
        user.save()
    context = {
        'title': '收货地址',
        'user': user,
    }
    return render(request, 'df_user/user_center_site.html', context)


def logout(request):
    request.session.flush()
    return redirect(reversed('df_goods:index'))
