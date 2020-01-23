from alipay import AliPay
from Shopping_website.settings import alipay_private_key, alipay_public_key, appid


def getUrl(params):
    """
    :params = {
        "order_no":"订单",
        "money":"100"
    }
    :param params:
    :return:
    """
    ali_pay = AliPay(
        # app id
        appid=appid,
        ## app通知地址
        app_notify_url=None,
        # 公钥 字符串
        app_private_key_string=alipay_private_key,
        # 私钥
        alipay_public_key_string=alipay_public_key,
    )

    # 构建支付订单信息
    order_info = ali_pay.api_alipay_trade_page_pay(
        subject="军火生意",  # 交易主题
        out_trade_no=params.get('order_no'),  # 订单号
        total_amount=str(params.get('money')),  # 交易 金额  字符串
        return_url="http://127.0.0.1:8000/store/payresult/",  # 回调地址
        notify_url=None  # 通知地址
    )

    # 返回支付宝的链接
    url = 'https://openapi.alipaydev.com/gateway.do?' + order_info
    return url
    # print(url)