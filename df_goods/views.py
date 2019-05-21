from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
from df_cart.models import Cart
from haystack.views import SearchView

GOODS_NUM = 1


def index(request):
    typelist = models.TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type00 = typelist[0].goodsinfo_set.order_by('-sale')[0:4]
    type01 = typelist[1].goodsinfo_set.order_by('-sale')[0:4]
    type02 = typelist[2].goodsinfo_set.order_by('-sale')[0:4]
    type03 = typelist[3].goodsinfo_set.order_by('-sale')[0:4]
    type04 = typelist[4].goodsinfo_set.order_by('-sale')[0:4]
    type05 = typelist[5].goodsinfo_set.order_by('-sale')[0:4]
    cart_num = 0
    if request.session.get('user_id'):
        cart_num = Cart.objects.filter(user_id=request.session['user_id']).count()
    context = {
        'title': '首页', 'guest_cart': 1,
        'type0': type0, 'type00': type00,
        'type1': type1, 'type01': type01,
        'type2': type2, 'type02': type02,
        'type3': type3, 'type03': type03,
        'type4': type4, 'type04': type04,
        'type5': type5, 'type05': type05,
        'cart_num': cart_num,
    }
    return render(request, 'df_goods/index.html', context)


def good_list(request, type_id, page_id, sort_id):
    goods_type = models.TypeInfo.objects.get(pk=type_id)  # 获取商品种类
    news = goods_type.goodsinfo_set.order_by('-id')[0:2]  # 获取该种类中最新的两个商品
    goods_list = models.GoodsInfo.objects.filter(type_id=type_id)  # 获取该种类的所有商品
    if sort_id == 1:
        goods_list = goods_list.order_by('-id')  # 按上架时间排序
    elif sort_id == 2:
        goods_list = goods_list.order_by('-price')  # 按价格排序
    elif sort_id == 3:
        goods_list = goods_list.order_by('-sale')  # 按销量排序
    pages = Paginator(goods_list, GOODS_NUM)  # 分页，没页放GOODS_NUM个商品
    page = pages.page(page_id)  # 获取第page_id页
    cart_num = 0
    if request.session.get('user_id'):
        cart_num = Cart.objects.filter(user_id=request.session['user_id']).count()
    context = {
        'title': goods_type.title,
        'page': page,
        'pages': pages,
        'goods_type': goods_type,
        'sort_id': sort_id,
        'news': news,
        'cart_num': cart_num,
    }
    return render(request, 'df_goods/list.html', context)


def goods_detail(request, goods_id):
    goods = models.GoodsInfo.objects.get(pk=goods_id)
    goods.sale += 1
    goods.save()
    news = goods.type.goodsinfo_set.order_by('-id')[0:2]
    cart_num = 0
    if request.session.get('user_id'):
        cart_num = Cart.objects.filter(user_id=request.session['user_id']).count()
    context = {
        'title': goods.type.title,
        'goods': goods,
        'news': news,
        'goods_id': goods_id,
        'cart_num': cart_num,
    }
    response = render(request, 'df_goods/detail.html', context)
    # 记录最近浏览，在用户中心使用
    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_id = '%d' % goods.id
    if goods_ids != '':  # 判断是否有浏览记录，如果有则继续判断
        goods_ids1 = goods_ids.split(',')  # 拆分为列表
        if goods_ids1.count(goods_id) >= 1:
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0, goods_id)  # 添加到第一个
        if len(goods_ids1) >= 6:  # 如果超过6个则删除最后一个
            del goods_ids1[5]
        goods_ids = ','.join(goods_ids1)
    else:
        goods_ids = goods_id  # 如果没有浏览记录则直接加
    response.set_cookie('goods_ids', goods_ids)  # 写入cookie

    return response


class MySearchView(SearchView):
    def extra_context(self):
        context = super(MySearchView, self).extra_context()
        context['title'] = '搜索'
        context['cart_count'] = 0
        if self.request.session.get('user_id', ''):
            cart_num = Cart.objects.filter(user_id=self.request.session['user_id']).count()
            context['cart_num'] = cart_num
        return context
