import urllib.request
import re

# cursorid，这是第一页的cursor而不是last
cid='6361537946612933091'
# 分析中最后一个+1的无关紧要，url中直接去掉dawdawdaAWDAdawdAwDasdadAwdawDaWdAwda

for i in range (0,100):
	print('第'+str(i+1)+'页评论数据')
	# 更新url
	url='https://video.coral.qq.com/varticle/2060051377/comment/v2?callback=_varticle2060051377commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+str(cid)+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132'

	data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
	# 匹配content后面的值，即双引号内文本，注意加双引号
	pat1='"content":"(.*?)"'
	comment=re.compile(pat1,re.S).findall(data)
	# comment是一个list，可以分开输出
	for item in comment:
		print(str(item))
		# 如果输出为\u6211等字符编码，改为如下方式
		# print(eval('u"'+str(item)+'"'))
		print("------------"*3)

	# 更新cid，下一个数据入口
	pat2='"last":"(.*?)"'
	cid=re.compile(pat2,re.S).findall(data)[0]