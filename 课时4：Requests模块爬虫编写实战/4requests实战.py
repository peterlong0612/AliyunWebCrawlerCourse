import requests,re,time
# import math
key = 'Python'
url = "https://yq.aliyun.com/search/articles/"
data = requests.get(url,params={"q":key}).text
# pat1 = '找到(.*?)条关于'
pat1 = '<div class="_search-info">找到(.*?)条关于'
allline = re.compile(pat1,re.S).findall(data)[0]
# print(allline)
allpage = int(allline)//15 + 1
# allpage = math.ceil(alline/15)

for i in range(0 , int(allpage)):
	print("---------------正在爬取第"+str(i+1)+"页------------")
	index = str(i+1)
	getdata = {"q":key,
               "p":index
               }
	data = requests.get(url, params = getdata).text
	# 获取文章的连接,注意有多个-------15个
	pat_url = '<div class="media-body text-overflow">.*?<a href="(.*?)">'
	articles = re.compile(pat_url,re.S).findall(data)

	# 依次爬取每篇博文
	for j in articles:
		# 为什么要加这个[0]？因为re的结果是一个列表，这样去第一个元素，皆是字符串
		num = re.compile('articles/(.*?)$').findall(j)[0]

		thisUrl = 'https://yq.aliyun.com/'+j
		thisData = requests.get(thisUrl).text

		pat_title = '<p class="hiddenTitle">(.*?)</p>'
		pat_content = '<div class="content-detail unsafe markdown-body">(.*?)<div class="copyright-outer-line">'
		title = re.compile(pat_title,re.S).findall(thisData)[0]
		content = re.compile(pat_content,re.S).findall(thisData)[0]

		fh = open("D:\\PeterLong\\本科三级2020\\AliyunWebCrawlerCourse\\课时4：Requests模块爬虫编写实战\\实战爬取博文\\"+str(i)+'_'+num+'_'+str(time.time())+'.html','w+',encoding='utf-8')
		fh.write(title + "<br /><br />" + content)
		fh.close()