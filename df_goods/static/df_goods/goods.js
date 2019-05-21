function add() {
    num = parseInt($('.num_show').val());
    $('.num_show').val(num + 1);
    $('.num_show').blur();
}

function minus() {
    num = parseInt($('.num_show').val());
    $('.num_show').val(num - 1);
    $('.num_show').blur();
}

$(function () {
    $('.num_show').blur(function () {
        num = parseInt($('.num_show').val());
        if (num < 1) {
            num = 1;
        }
        price = parseFloat($('#price').text());
        total = num * price;
        $('.num_show').val(num);
        $('#total').text(total.toFixed(2) + '元');
    });
});


var $add_x = $('#add_cart').offset().top;
var $add_y = $('#add_cart').offset().left;

var $to_x = $('#show_count').offset().top;
var $to_y = $('#show_count').offset().left;

$(".add_jump").css({'left': $add_y + 80, 'top': $add_x + 10, 'display': 'block'})
$('#add_cart').click(function () {
    // 判断是否登录，若未登录，则提示先登录
    if ($('.login_btn').text().indexOf('登录') >= 0) {
        alert('请先登录后再购买');
        location.href = '/user/login/';
        return;
    }
    // 动画
    $(".add_jump").stop().animate({
            'left': $to_y + 7,
            'top': $to_x + 7
        },
        "fast", function () {
            $(".add_jump").fadeOut('fast', function () {
                $('#show_count').html(2);
            });
        });
})