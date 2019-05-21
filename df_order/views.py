from django.shortcuts import render, HttpResponse, reverse, redirect
from django.db import transaction
from django.http import JsonResponse

from decimal import Decimal

from df_user import user_decorator
from df_user.models import UserInfo
from df_cart.models import Cart
from .models import Order, OrderDetail


@user_decorator.login
def show_order(request):
    user_id = request.session['user_id']        # 获取用户id
    user = UserInfo.objects.get(id=user_id)     # 获取用户
    cart_ids = request.GET.getlist('cart_id')   # 获取购物车参数
    carts = []                  # 购物车
    total_price = 0             # 总价格
    for cart_id in cart_ids:    # 购物车id
        cart = Cart.objects.get(id=cart_id)
        carts.append(cart)
        total_price += cart.count * cart.goods.price
    trans_cost = 10
    total_trans_price = trans_cost + total_price
    context = {
        'title': '提交订单',
        'page_name': 1,
        'user': user,       # 用户
        'carts': carts,     # 购物车列表
        'total_price': total_price,  # 商品总价值
        'trans_cost': trans_cost,    # 运费
        'total_trans_price': total_trans_price,     # 实际总价格
    }
    return render(request, 'df_order/place_order.html', context)


'''
事务提交：
这些步骤中，任何一环节一旦出错则全部退回1
1. 创建订单对象
2. 判断商品库存是否充足
3. 创建 订单 详情 ，多个
4. 修改商品库存
5. 删除购物车
'''


@transaction.atomic()
@user_decorator.login
def order_handle(request):
    user_id = request.session['user_id']
    user = UserInfo.objects.get(id=user_id)
    if not user.full_name or not user.phone or not user.address:
        return redirect(reverse('df_user:site'))
    tran_id = transaction.savepoint()  # 保存事务发生点
    cart_ids = request.POST.get('cart_ids')  # 用户提交的订单购物车，此时cart_ids为字符串，例如'1,2,3,'
    user_id = request.session['user_id']  # 获取当前用户的id
    sign = {}
    try:
        user = UserInfo.objects.get(pk=user_id)
        order = Order()  # 创建一个订单对象
        order.user = user  # 订单的用户
        order.address = user.address + "（%s）" % user.full_name + user.phone
        order.total = Decimal(request.POST.get('total'))  # 从前端获取的订单总价
        order.save()  # 保存订单

        for cart_id in cart_ids.split(','):  # 逐个对用户提交订单中的每类商品即每一个小购物车
            cart = Cart.objects.get(pk=cart_id)  # 从CartInfo表中获取小购物车对象
            order_detail = OrderDetail()  # 大订单中的每一个小商品订单
            order_detail.order = order  # 外键关联，小订单与大订单绑定
            goods = cart.goods  # 具体商品
            if cart.count <= goods.stock:  # 判断库存是否满足订单，如果满足，修改数据库
                goods.stock = goods.stock - cart.count
                goods.save()
                order_detail.goods = goods
                order_detail.price = goods.price
                order_detail.count = cart.count
                order_detail.save()
                cart.delete()  # 并删除当前购物车
            else:  # 否则，则事务回滚，订单取消
                transaction.savepoint_rollback(tran_id)
                return HttpResponse('库存不足')
        sign['ok'] = 1
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print("=========%s==========" % e)
        print('未完成订单提交')
        transaction.savepoint_rollback(tran_id)  # 事务任何一个环节出错，则事务全部取消
    return JsonResponse(sign)


@user_decorator.login
def pay(request, order_id):
    cart_num = Cart.objects.filter(user_id=request.session['user_id']).count()
    order = Order.objects.get(id=order_id)
    total = order.total
    context = {
        'title': '付款',
        'total': total,
        'cart_num': cart_num,
    }
    return render(request, 'df_order/pay.html', context)
