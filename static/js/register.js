$(function () {

    var error_name = false;             // 用户名错误标记
    var error_password = false;         // 密码错误标记
    var error_check_password = false;   // 确认密码错误标记
    var error_email = false;            // 邮箱错误标记
    var error_check = false;            // 同意协议错误标记

    // 当id='user_name'属性的元素失去焦点时，触发check_user_name()事件
    $('#user_name').blur(function () {
        check_user_name();
    });

    // 当id='pwd'属性的元素失去焦点时，触发check_pwd()事件
    $('#pwd').blur(function () {
        check_pwd();
    });

    // 当id='cpwd'属性的元素失去焦点时，触发check_cpwd()事件
    $('#cpwd').blur(function () {
        check_cpwd();
    });

    // 当id='email'属性的元素失去焦点时，触发check_email()事件
    $('#email').blur(function () {
        check_email();
    });

    // 当id='allow'属性的元素被点击后
    $('#allow').click(function () {
        if ($(this).is(':checked')) {   // 如果当前所选的元素是':checked'
            error_check = false;        // 已选择
            $(this).siblings('span').hide(); // 隐藏同级span元素内容
        } else {
            error_check = true;         // 未选择
            $(this).siblings('span').html('请勾选同意'); // 改变同级span元素的内容为'请勾选同意'
            $(this).siblings('span').show();            // 显示同级span元素的内容
        }
    });


    function check_user_name() {
        var len = $('#user_name').val().length;
        if (len < 2 || len > 20) {
            $('#user_name').next().html('请输入2-20个字符的用户名')
            $('#user_name').next().show();
            error_name = true;
        } else {
            $.get('/user/register_exist/?username=' + $('#user_name').val(), function (data) {
                if (data.count == 1) {
                    $('#user_name').next().html('用户名已存在').show();
                    error_name = true;
                } else {
                    $('#user_name').next().hide();
                    error_name = false;
                }
            });
        }
    }

    function check_pwd() {
        var len = $('#pwd').val().length;
        if (len < 8 || len > 20) {
            $('#pwd').next().html('密码最少8位，最长20位')
            $('#pwd').next().show();
            error_password = true;
        } else {
            $('#pwd').next().hide();
            error_password = false;
        }
    }

    // 定义JavaScript函数
    function check_cpwd() {
        var pass = $('#pwd').val();     // 获取输入的密码
        var cpass = $('#cpwd').val();   // 获取输入的确认密码

        if (pass != cpass) {            // 如果确认密码与输入密码不同
            $('#cpwd').next().html('两次输入的密码不一致');    // 改变提示信息为'两次输入的密码不一致'
            $('#cpwd').next().show();                       // 显示密码不同提示
            error_check_password = true;
        } else {
            $('#cpwd').next().hide();       // 如果两次密码输入相同，隐藏提示信息
            error_check_password = false;
        }
    }

    // 验证邮箱
    function check_email() {
        var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

        if (re.test($('#email').val())) {
            $('#email').next().hide();
            error_email = false;
        } else {
            $('#email').next().html('你输入的邮箱格式不正确')
            $('#email').next().show();
            error_check_password = true;
        }
    }

    // 检查表单
    $('#reg_form').submit(function () {
        check_user_name();
        check_pwd();
        check_cpwd();
        check_email();
        // 返回布尔值
        return !(error_name || error_password || error_check_password || error_email || error_check)
    });
});
