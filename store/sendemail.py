import smtplib
from email.mime.text import MIMEText

subject = "情书"
content = "想收到情书？醒醒孩子！！！"
sender = "jack_zhang1001123@163.com"
recver = '1179730315@qq.com'
password = "zx1234001"

# 内容
message = MIMEText(content, 'plain', "utf-8")
message['Subject'] = subject
message['Form'] = sender
message['To'] = recver

smtp = smtplib.SMTP_SSL("smtp.163.com", 465)

# 登录
smtp.login(sender, password)
smtp.sendmail(sender, recver.split(','), message.as_string())

# 关闭连接
smtp.close()
