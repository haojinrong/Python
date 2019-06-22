str_ = open('res1.txt'，"rb").read()
results = res1.findall('http://www.baidu.com/s?',s)
open("urls.txt","wb").write("\r\n".joint(results))
        for res1 in split_:
            if 'http' in res1 or 'https' in res1i:
                url = res1.split('"')[1]
                if 'jpg' in url:
                    URLS.append(url)

for url in URLS:
    response = requests.get(url)
    content = response.content
    name = url.split('/')[-1]

with open(res1,'wb') as f:
        f.write(content)


import requests
URLS=[]
url='http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response=requests.get(url)
HTML=response.text
URLS = HTML.split('\n')
for url in URLS:
    response=requests.get(url)
    content=response.content
    name=url.split('/')[-1]
with open(response.text,'wb') as f:
    f.write(content)



