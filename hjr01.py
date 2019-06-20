import urllib.request
import random

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
url = 'http://baidu.com'
proxy_handle = [{'http://1.198.73.189:9999'},{'http://111.226.211.11:8118'},{'http://175.181.40.199:44308'}]
while 1:
    print(proxy_handle.pop())
    print(proxy_handle)
    if len(proxy_handle) ==0:
        print('爬取失败')
proxy = urllib.request.ProxyHandler(proxy_handle)
opener = urllib.request.build_opener(proxy_handle)
reponse = opener.open(url)
print(reponse.read())