import re

str11='aliyunedu'
pat11='yu'

str12='aliyun\nedu'
pat12='yun\n'

str13='aliyu89787nedu'
pat13='\w\d\w\d\d\w'

strs1=[str11,str12,str13]
pats1=[pat11,pat12,pat13]
print('实例1')
for i in range(3):
	print(f'\n匹配方式：re.compile(\'{pats1[i]}\').findall(\'{strs1[i]}\')\n匹配结果：',re.compile(pats1[i]).findall(strs1[i]))
print('\n==================================================================\n')

########

str2='aliyunnnnji87362387aoyubaidu'
pat21='ali...'
pat22='^li...'
pat23='bai..$'
pat24='ali.*'
pat25='aliyun+'
pat26='aliyun?'
pat27='yun{1,2}'
pat28='^al(i..)'
pats2=[pat21,pat22,pat23,pat24,pat25,pat26,pat27,pat28]
print('实例2')
for i in range(8):
	print(f'\n匹配方式：re.compile(\'{pats2[i]}\').findall(\'{str2}\')\n匹配结果：',re.compile(pats2[i]).findall(str2))
print('\n==================================================================\n')

#######贪婪、懒惰模式

str3='poythonyhjskjsa'
pat31='p.*y'
pat32='p.*?y'

print('实例3——贪婪、懒惰模式\n'+'源字符串：poythonyhjskjsa')
print(f'\n匹配方式：re.compile(\'{pat31}\').findall(\'{str3}\')\n匹配结果：',re.compile(pat31).findall(str3))
print(f'\n匹配方式：re.compile(\'{pat32}\').findall(\'{str3}\')\n匹配结果：',re.compile(pat32).findall(str3))

print('\n==================================================================\n')

#######模式修正符
print('实例4——模式修正符\n'+'源字符串:Pyhon\n')
str41='Python'
print(f'\n匹配方式：re.compile(\'pyt\').findall(\'{str41}\')\n','匹配结果：',re.compile('pyt').findall(str41))
print(f'\n匹配方式：re.compile(\'pyt\',re.I).findall(\'{str41}\')\n','匹配结果：',re.compile('pyt',re.I).findall(str41))

str42='''我是阿里云大学
欢迎来学习
Pyhon网络爬虫课程
'''
pat42="阿里.*?Python"
print('\n源字符串:'+str42)
print(f'\n匹配方式：re.compile(\'{pat42}\').findall(\'{str42}\')\n','匹配结果：',re.compile(pat42).findall(str42))
print(f'\n匹配方式：re.compile(\'{pat42}\',re.S).findall(\'{str42}\')\n','匹配结果：',re.compile(pat42,re.S).findall(str42))