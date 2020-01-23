from alipay import AliPay
from Shopping_website.settings import alipay_public_key, alipay_private_key, appid


def aliPay(order_id, order_price):
    ## 公钥

    ## 2. 实例化一个支付对象
    ali_pay = AliPay(
        ## app id
        appid= appid,
        ## app 通知地址
        app_notify_url=None,
        ## 私钥  字符串
        app_private_key_string=alipay_private_key,
        ## 公钥
        alipay_public_key_string=alipay_public_key,
    )

    ## 3. 构建支付订单信息
    ## 网页支付
    order_info = ali_pay.api_alipay_trade_page_pay(
        subject="沙箱支付",  ### 交易的主题
        out_trade_no=order_id,  ### 订单号
        total_amount=order_price,  ### 交易金额  字符串
        return_url="http://127.0.0.1:8000/shop/index/",  ### 回调地址
        notify_url="http://127.0.0.1:8000/shop/index/",  ## 通知地址
    )

    ##  4. 返回支付宝支付链接
    url = "https://openapi.alipaydev.com/gateway.do?" + order_info

    return url
