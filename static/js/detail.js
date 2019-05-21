

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

