a=1

s = """
href=xxxhref=sahref=\\"\\/p\\/1005055652790996\\/myfollow?t=1&pids=Pl_Official_RelationMyfollow__95&cfs=&Pl_Official_RelationMyfollow__95_page=2#Pl_Official_RelationMyfollow__95
"""

import re
next_page = re.findall('.+(href=(?:.*)Pl_Official_RelationMyfollow__95)', s)    #匹配 最后一个href= 后加任意字符 并且以最后一个Pl_Official_RelationMyfollow__95为结尾的字符串
print(next_page)

s = 'src=wadad.jpg//src=sadasdada.gif123123assrc=dhaui.jpg'
x=re.findall('src=(.*?[jg][pi][gf])',s)              #匹配以jpg或gif为结尾的字符串
print(x)
x=re.findall('src=(.*?(?:jpg|gif))',s)
print(x)



s = 'srcsrcsrcsrc'
x=re.findall('(?:src)?src',s)
print(x)



s = "\\"
print(s)

