import smtplib
from email.mime.text import MIMEText # 邮件正⽂
from email.header import Header # 邮件头
# 登录邮件服务器
smtp_obj = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
# 发件⼈邮箱中的SMTP服务器，端⼝是25
smtp_obj.login("nami@luffycity.com", "xxxx-sd#gf")
# 括号中对应的是发件⼈邮箱账号、邮箱密码

#smtp_obj.set_debuglevel(1) # 显示调试信息
# 设置邮件头信息
msg = MIMEText("Hello, ⼩哥哥，约么？800上⻔，新到学⽣妹...", "plain", "utf-8")
msg["From"] = Header("来⾃娜美的问候","utf-8") # 发送者
msg["To"] = Header("有缘⼈","utf-8") # 接收者
msg["Subject"] = Header("娜美的信","utf-8") # 主题
# 发送
smtp_obj.sendmail("nami@luffycity.com", ["alex@luffycity.com",
"317822232@qq.com"], msg.as_string())