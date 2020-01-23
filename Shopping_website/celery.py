from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.conf import settings

# 设置 celery的工作目录
os.environ.setdefault('DJANGO.SETTINGS_MODULE', 'Shopping_website.settings')

# 实例化celery
app = Celery('Shopping_website')

# celery 配置的来源

app.config_from_object('django.conf.settings')

# 如果在app当中 有创建tasks.py 就会自动检索
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
