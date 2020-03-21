# 实战：批量爬取糗事百科段子数据
# 目标站点：https://www.qiushibaike.com
# 目标数据：热门段子
# 要求：实现自动翻页

import urllib.request
import re
import random
import time

# 用户代理池，伪装升级
uapools=[
	"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
	"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
	]

def UAfun():
	opener=urllib.request.build_opener()
	thisUA=random.choice(uapools)
	UA=("User-Agent",thisUA)
	opener.addheaders=[UA]
	# 安装为全局，让urlopen也可以实现伪装
	urllib.request.install_opener(opener)
	#data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
	print("当前使用UA："+str(thisUA))

for i in range(622):
	UAfun()
	thisUrl='http://www.qiushibaike.net/'+str(f'{i+1:0>6}')+'.html'
	try:
		data=urllib.request.urlopen(thisUrl).read().decode("GBK","ignore")
		#data=urllib.request.urlopen(thisUrl).read().decode("utf-8","ignore")
		
		pat='<div class="content">(.*?)</div>'
		rst=re.compile(pat,re.S).findall(data)
		for j in range(0,len(rst)):
			print(rst[j])
			print("----------"*5)
	except Exception as err:
		pass