 #爬取http://www.17k.com/chapter/2933095/36699279.html存入本地
import urllib.request
url = 'http://www.17k.com/chapter/2933095/36699279.html'
#创建request
request=urllib.request.Request(url)
#发送请求获取结果
response = urllib.request.urlopen(request)
data = response.read()
data = data.decode('utf-8')
print (data)
#爬取数据保存到文件
filename = open(url,encoding='utf-8')
filename.write(htmldata)
filename.close()