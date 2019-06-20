import urllib.request

urls = ('http://httpbin.org/get'，'http://www.baidu.com/get'，'http://www.souhu.com')
for url in urls:
    response = urllib.request.urlopen(url)
    print(response.status)
    if response.status ==200:
        print('%s 该网站继续爬')
    else：
        print('%s错误')