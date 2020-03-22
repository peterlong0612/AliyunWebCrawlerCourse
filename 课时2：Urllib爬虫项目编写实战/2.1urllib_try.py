import urllib.request
data=urllib.request.urlopen("http://www.jd.com").read().decode("utf-8","ignore")
print(len(data))

import re
pat="<title>(.*?)</title>"
print("爬到内存：",re.compile(pat,re.S).findall(data))

# 爬到硬盘中
#urllib.request.urlretrieve("http://www.jd.com",filename="D:\\PeterLong\\本科三级2020\\AliyunWebCrawlerCourse\\课时2：Urllib爬虫项目编写实战\\jd.html")

# 浏览器伪装
# 尝试
url="https://www.qiushibaike.com/"
# data=urllib.request.urlopen(url).read().decode("utf-8","ignore")

User_Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
# opener添加高级设置的对象
opener=urllib.request.build_opener()
UA=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36")
opener.addheaders=[UA]
# 安装为全局，让urlopen也可以实现伪装
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
print(len(data))

# 用户代理池，伪装升级
uapools=[
	"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
	"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"
	]

import random
def UAfun():
	opener=urllib.request.build_opener()
	thisua=random.choice(uapools)
	ua=("User-Agent",thisua)
	opener.addheaders=[UA]
	# 安装为全局，让urlopen也可以实现伪装
	urllib.request.install_opener(opener)
	#data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
	print("当前使用UA："+str(thisua))

url="https://www.qiushibaike.com/"
for i in range(0,10):
	UAfun()
	data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
	print(i+len(data))
# 如何实践每爬3次换一次UA
for j in range(1,10):
	if j%3==0:
		UAfun()
	data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
	print(j+len(data))

# 实战：批量爬取糗事百科段子数据
# 目标站点：https://www.qiushibaike.com
# 目标数据：热门段子
# 要求：实现自动翻页

# for i in range(3):
# 	print(str(f'{i+1:0>6}'))