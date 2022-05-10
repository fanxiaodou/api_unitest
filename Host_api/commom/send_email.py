"""
email.py 配置收发邮件
"""
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import time
import os


def send_mail(new_report):
    f = open(new_report, "rb")
    mail_body = f.read()
    f.close()
    message = MIMEText(mail_body, "html", "utf-8")
    '''
    QQ邮箱的 发件人 用户名 密码  收件人邮箱 群发 
    '''
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1111111@qq.com"  # 用户名
    mail_pass = "xxxxxxxx"  # 口令

    sender = "1111111@qq.com@qq.com"
    receivers = ["1111111@qq.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message["Subject"] = Header("自动化测试报告", "utf-8").encode()
    message["From"] = Header(sender)
    message["To"] = Header(("测试负责人 <%s>" % receivers))
    message["date"] = time.strftime("%a,%d %b %Y %H:%M:%S %z")

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    return file_new


if __name__ == '__main__':
    report_path = r'C:\Users\86182\Desktop\unitest_ui_web\Host_api\report'
    new_report1 = new_report(report_path)
    send_mail(new_report1)
