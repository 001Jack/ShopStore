from alipay import AliPay

alipay_public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArye9AhzRw1zSwwZ+4c0cD9Cg82lSJBRPHyvvBGwFsnJ/TJOjo4zQOpHTz0/d3IfpMCvQI4JIw93ws1v+bJWgB/XDgiwjIpT8pqFVlvLPVTXNlmBdpFNXtMFlai5DHIKogfuBmswH6v/ZcpVprB7DHAvUmhkTjpemdHs1eWceXfHadM+L1EbrqjpSduyRwRA1pPCqKjnoe4H5pk2jQZL+uOQss3G7FzN56tpXaNSEFmKBgNPu4TXbMt3QjxkS3Rl9b2nOOW1EcoO38G/cfxCSWnqJEIaIPYNPCS6f7xoABLxlX+PF54aLPoyNWIj6bnfuJhkwzXeAx6fliE9QI7aoLQIDAQAB
-----END PUBLIC KEY-----"""
alipay_private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEArye9AhzRw1zSwwZ+4c0cD9Cg82lSJBRPHyvvBGwFsnJ/TJOjo4zQOpHTz0/d3IfpMCvQI4JIw93ws1v+bJWgB/XDgiwjIpT8pqFVlvLPVTXNlmBdpFNXtMFlai5DHIKogfuBmswH6v/ZcpVprB7DHAvUmhkTjpemdHs1eWceXfHadM+L1EbrqjpSduyRwRA1pPCqKjnoe4H5pk2jQZL+uOQss3G7FzN56tpXaNSEFmKBgNPu4TXbMt3QjxkS3Rl9b2nOOW1EcoO38G/cfxCSWnqJEIaIPYNPCS6f7xoABLxlX+PF54aLPoyNWIj6bnfuJhkwzXeAx6fliE9QI7aoLQIDAQABAoIBAEfD3GlVLY0CJ0jJDIuv4mOIc6nH6WPm/lQjSBdjuyHWT9osU8vbEiYtQb+bVafZ9+1IxksGQpIeCVUzyBbtZ1hblfNr6iltKeeMCumCKvkaxlVqvnNpwnHJG6hZtB2mWyyGxB+MoWHj2lBcb6OaJw8CueU5iQ3PjOAE63AGlCahFsWL5yxr82qSx0FIVT++4jd/rva71CmhPCFvue/6uOnZm9gzBq/CJ2i7GpWglmTfxXb3joS2FVVuReEh98PPtvWR0FEW2KA27GNKDCnTSYfCM8h9iusELOxGuNrlRzgyo+yHlKXLugy5UJUykit6IIR4eCRPjWlYIe0vSnrfKPECgYEA7nHBfj2XXvTpnprhD+5A446h5zLmguEGAqeMce9NhnVufcolvwjQ7m3m7G8ddQW5yOu6QrZBTtENYvr+mb81NYgu6t2Vl07MdtDGsvLKpL+9HXdgkREoxayR7qo9upKeiGo9oOjtp194RIrYOQLb7jhXIS329wjn30MoKMFlRwMCgYEAvA0Y1qIO7T3ukFr2R6q6jnhfZzC6+2I4ytj22sIAIcSZSP9ZfrfZRFbA+Mra589teaI1fzRBJFrDUPHg9QATPJphdnStI7XG7A/F/18z70DbvfGvXxXwXpHtmqO4SjLVQMRE2dsDhFbKexRc05dY65290nw67OMxQQ/KX+rm1Q8CgYBZzua+EZyt2zkSz+rtASPXkaVRW06PBQoqfcjcMPHWLuzK3BSTe1KWOza63q8NoHZ1QrQI5HR8pyiPm1HBvs7ftsdVFth9AOTp64Crbd79ZmpoasooWXot2e2tItnVJ9wmLT3BGXpJjB/UUSdXccg8VWQbzyAxs10CLl013IG02QKBgBSwNC1Ywt+i0p4bA8E6rS+DWquVltyVH75hRDco5K7SXDLFtOjV/RchnDVCy/Z4wYiCKfSGoSwIuDgthBwwF+2w5kwL5ghptSq/SX8g0CvgLMymzC5f0YP19ffvTxUKpp9reE+nYqmqirgjs1qr6eJyBjIj7K+nBwIrZI5M33xNAoGAV69MTdHtCfpiyULIkCnATEDc/v8Nw+MmzyZmnQ59rrjVYX4XYP84UWZA6VsNi155FLKI6Iavagz1XdUqliRsEmXzxHf0tYheaklHG3guO+q4r+ydwn4rLPDpnAlC6XRzpdqaKdUB2olfssgZkkt48ofZueLanmn878K/DVLnO/Q=
-----END RSA PRIVATE KEY-----"""

# 实例化一个支付对象
ali_pay = AliPay(
    # app id
    appid="2016100100640637",
    ## app通知地址
    app_notify_url=None,
    # 公钥 字符串
    app_private_key_string=alipay_private_key,
    # 私钥
    alipay_public_key_string=alipay_public_key,
)

import time


def get_order():
    order = str(time.time()).replace('.', '')
    return order


# 构建支付订单信息
order_info = ali_pay.api_alipay_trade_page_pay(
    subject="军火生意",  # 交易主题
    out_trade_no=get_order(),  # 订单号
    total_amount='10',  # 交易 金额  字符串
    return_url=None,  # 回调地址
    notify_url=None  # 通知地址
)

# 返回支付宝的链接
url = 'https://openapi.alipaydev.com/gateway.do?' + order_info
print(url)
