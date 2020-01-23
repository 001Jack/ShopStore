from __future__ import absolute_import

import json
import smtplib
from email.mime.text import MIMEText

import requests

from Shopping_website.celery import app


@app.task
def add(x, y):
    print(x + y)
    return x + y


@app.task
def add_v1():
    print("来个定时任务让我瞅一瞅！")


@app.task
def sendDing(content):
    headers = {
        "Content-Type": "application/json"
    }
    data = {

            "msgtype": "text",
            "text": {
                "content": content,
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
