from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from .models import Cart
from df_user import user_decorator


@user_decorator.login
def cart(request):
    user_id = request.session['user_id']
    carts = Cart.objects.filter(user_id=user_id)
    context = {
        'title': '购物车',
        'page_id': 1,
        'carts': carts,
    }
    return render(request, 'df_cart/cart.html', context)


@user_decorator.login
def add(request, goods_id, count):
    user_id = request.session['user_id']
    # 查询购物车中是否已经有此商品，如果有则数量增加，否则，新增
    carts = Cart.objects.filter(user_id=user_id, goods_id=goods_id)
    if carts:
        carts = carts[0]
        carts.count += count
    else:
        carts = Cart()
        carts.user_id = user_id
        carts.goods_id = goods_id
        carts.count = count
    carts.save()
    # 如果是ajax请求则返回json，否则转向购物车
    if request.is_ajax():
        count = Cart.objects.filter(user_id=request.session['user_id']).count()
        return JsonResponse({'count': count})
    else:
        return redirect(reverse('df_cart:cart'))


@user_decorator.login
def count_edit(request, cart_id, count):
    data = {}
    try:
        carts = Cart.objects.get(pk=cart_id)
        carts.count = count
        carts.save()
        data['count'] = 0
    except Exception as e:
        data['count'] = count
    return JsonResponse(data)


@user_decorator.login
def delete(request, cart_id):
    data = {}
    try:
        carts = Cart.objects.get(pk=cart_id)
        carts.delete()
        data['ok'] = 1
    except Exception as e:
        data['ok'] = 0
    return JsonResponse(data)
