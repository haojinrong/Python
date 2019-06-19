def function_name(panams):
    res = re.search("(.jpg|.JPG|.gif|.GIF|.bmp|.BMP|.png|.PNG|.jpeg|.JPEG)$",url)
import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'wd':'学生'},encoding='utf8')
print(data)
ur1='http://www.baidu.com/s?'+data
print(ur1)
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)


export default{
    data(){
        return{
            id:''
        }
        mounted : function(){
            this.id = this.route.params.tastId;
    }
}
data = bytes(urllib.parse.urlencode({'pw':'456','un':'756'}),enconding='utf8')
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url,data=data)
print(result)
