

'''
首先配置 Mail 邮件服务，然后才能发送邮件

'''


import os

from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    send_mail(
        '来自运维平台测试邮件',
        '欢迎注册运维管理系统用户,运维事故无大小，请谨慎！',
        'devops@wesine.com',
        ['xxx@qq.com'],
    )