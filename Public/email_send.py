#!/usr/bin/env python
# coding: utf-8
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib, time, os

def send_mali_by163(from_addr, password, mail_to, subject, path):
    # 实例化发送附件的对象
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['to'] = mail_to
    msg['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    report_obj = open(path, 'rb')
    mail_body_value = report_obj.read()
    mail_body = mail_body_value
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(mail_body_value)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(path))
    msg.attach(part)
    report_obj.close()
    # 正文
    body = MIMEText(mail_body, _subtype="html", _charset='utf-8')
    msg.attach(body)
    # 163邮件发送
    server = smtplib.SMTP_SSL("smtp.163.com", 465)
    server.login(from_addr, password)
    server.sendmail(from_addr, mail_to, msg.as_string())
    server.quit()

def send_mali_byQQ(from_addr, password, mail_to, subject, path):
    # 实例化发送附件的对象
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['to'] = mail_to
    msg['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    report_obj = open(path, 'rb')
    mail_body_value = report_obj.read()
    mail_body = mail_body_value
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(mail_body_value)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(path))
    msg.attach(part)
    report_obj.close()
    # 正文
    body = MIMEText(mail_body, _subtype="html", _charset='utf-8')
    msg.attach(body)
    # QQ邮件发送
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(from_addr, password)
    server.sendmail(from_addr, mail_to, msg.as_string())
    server.quit()
