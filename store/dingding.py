import requests
import json

# 构建 消息内容
headers = {
    "Content-Type": "application/json"
}

# data = {
#     "actionCard": {
#         "title": "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
#         "text":
#         "demo![screenshot](@lADOpwk3K80C0M0FoA) ### 乔布斯 20 年前想打造的苹果咖啡厅 Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划",
#         "hideAvatar": "0",
#         "btnOrientation": "0",
#         "btns": [
#             {
#                 "title": "内容不错",
#                 "actionURL": "https://www.dingtalk.com/"
#             },
#             {
#                 "title": "不感兴趣",
#                 "actionURL": "https://www.dingtalk.com/"
#             }
#         ]
#     },
#     "msgtype": "actionCard"
# }
# data = {
#      "msgtype": "markdown",
#      "markdown": {
#          "title":"demo杭州天气",
#          "text": "#### 杭州天气 @156xxxx8827\n" +
#                  "> 9度，西北风1级，空气良89，相对温度73%\n\n" +
#                  "> ![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png)\n"  +
#                  "> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n"
#      },
#     "at": {
#         "atMobiles": [
#             "156xxxx8827",
#             "189xxxx8325"
#         ],
#         "isAtAll": False,
#     }
#  }
data = {
    "feedCard": {
        "links": [
            {
                "title": "生活像一把无情刻刀demo",
                "messageURL": "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI",
                "picURL": "https://www.dingtalk.com/"
            },
            {
                "title": "论老齐头发为什么这么少",
                "messageURL": "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI",
                "picURL": "https://www.dingtalk.com/"
            }
        ]
    },
    "msgtype": "feedCard"
}


# url = "https://oapi.dingtalk.com/robot/send?access_token=7b726bf8bf72aa289c4514e759c4ba162057fd6227ec114f8e6cca127e8d8a43"
#
# data = json.dumps(data)
#
# response = requests.post(url, headers=headers, data=data)
#
# print(response.content.decode())


def sendDing():
    headers = {
        "Content-Type": "application/json"
    }
    data = {

        "msgtype": "text",
        "text": {
            "content": "demo大哥是个sb"
        },
        "at": {
            "atMobiles": [

            ],
            "isAtAll": False
        }
    }

    url = "https://oapi.dingtalk.com/robot/send?access_token=2bd6f6f8f352ba3534e763c22ede0fead136177f0a290c85fe067c3bc7448833"

    data = json.dumps(data)

    response = requests.post(url, headers=headers, data=data)

    print(response.content.decode())

