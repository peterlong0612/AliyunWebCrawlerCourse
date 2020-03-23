# 4 Requests模块基础
import requests
import re

# urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed:
# unable to get local issuer certificate (_ssl.c:1045)>
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 伪装浏览器
hd={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
# 需要开Fiddler才能使用这个ip+端口，因为fiddler才是代理，没有真正的代理的话最好关闭掉
# 检查一下电脑的网络设置，有没有正在使用这个端口，有的话需要关掉，避免占用
# 发现打开Fiddler之后，系统会自动设置代理，出现SSL等报错，解决之前建议把Fiddler关掉，并跳过代理这一部分
px={"http":"http://127.0.0.1:8888"}   

ck={"Cookie":"cna=TIw4FpgX0CACAd9IKOL7gIb0; isg=BAMDdrbaWRKJZBXmFhesQA7MkseteJe6z1KxRTXgX2LZ9CMWvUgnCuHmaoS6z--y"}


# rst=requests.get('http://www.aliwx.com.cn/',headers=hd)
# title=re.compile('<title>(.*?)</title>',re.S).findall(rst.text)

# print('rst: ',rst)
# print('title: ',title)

pr={"wd":"阿里文学"}
bd=requests.get("http://www.baidu.com/s",params=pr)
print('bd: ',bd)
print('bd.cookies: ',bd.cookies)
# cookies转换成字典
print('requests.utils.dict_from_cookiejar(bd.cookies):',requests.utils.dict_from_cookiejar(bd.cookies))
print('bd.url:',bd.url)
print('bd.encoding:',bd.encoding)
print('type(bd.content): ',type(bd.content))
print('type(bd.text): ',type(bd.text))
print('bd.status_code: ',bd.status_code)


# post

url = 'http://www.iqianyue.com/mypost/'
postdata = {"name":"测试账号","pass":"测试密码"}
rst = requests.post(url,data =postdata )

print('post----------------')
print('rst: ',rst)
print('text: ',rst.text)
