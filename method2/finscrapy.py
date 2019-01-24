from apscheduler.schedulers.blocking import BlockingScheduler
from email.header import Header
from email.mime.text import MIMEText
import time
import smtplib
import pymongo
import os

def send_email(collection):
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', 25)
    smtp.login('nickery_c@163.com', 'longwuxin0131')
    collection = collection + '数据已有更新请查看'
    msg = MIMEText(collection, 'plain', 'utf-8')
    msg['From'] = 'nickery<nickery_c@163.com>'
    msg['To'] = 'longwuxin'
    msg['Subject'] = Header('更新提醒', 'utf-8').encode()
    smtp.sendmail('nickery_c@163.com', ['nickery_c@163.com', '584860386@qq.com'], msg.as_string())
    smtp.quit()

def job_1():
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client['finscrapy']
    FR = db['FR']
    data_fr = FR.find_one(sort=[('_id', 1)])
    os.system('scrapy crawl FR')
    data_FR = FR.find_one(sort=[('_id', 1)])
    time_FR = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(time_FR, ':已检查FR数据')
    if data_fr != data_FR:
        date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print(date, ':FR数据有更新，已发送邮件')
        collection = 'FR'
        send_email(collection)
    ECB = db['ECB']
    data_ecb = ECB.find_one(sort=[('_id', 1)])
    os.system('scrapy crawl ecb')
    data_ECB = ECB.find_one(sort=[('_id', 1)])
    time_ECB = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(time_ECB, ':已检查ECB数据')
    if data_ecb != data_ECB:
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(date, ':ECB数据有更新，已发送邮件')
        collection = 'ECB'
        send_email(collection)

sched = BlockingScheduler()
sched.add_job(job_1, 'interval', seconds=30, id='job_1')

try:
    sched.start()
except Exception as e:
    print('scheduler error:', e)
    sched.remove_job('job_1')