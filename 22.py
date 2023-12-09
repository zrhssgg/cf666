import requests
import pythonfofa
import sys
​
def userinfo(client):
#个人信息
info = client.userinfo()
print(info)
​
def write(results):
with open('ip.txt', 'a+') as fp:
for item in results:
ip = item[0]
country = item[1]
print(ip, country)
fp.write(ip+'|'+country+'\n')
​
def read():
for item in open('./ip.txt', 'r'):
#print(item)
item = item.split('|')
ip = item[0]
country = item[1].replace('\n', '')
print(country)
​
def get_ip(client):
​
for page in range(1, 2):
# 查询语句
query_str = 'port="54321" && title==" 登录 "'
field = ['ip','country_name']
​
#查询结果
#handle.search(query_text, field, page, size, full)
data = client.search(query_str,field=field, page=page,size=10000)
​
# noinspection PyBroadException
try:
results = data['results']
print(results)
except Exception as e:
print('运行错误，账号密码可能出错！')
print(data)
sys.exit(1)
#写入文件
write(results)
​
if __name__ == '__main__':
​
email, key = ('email','key')
client = pythonfofa.Client(email,key)
​
get_ip(client)
#read()
