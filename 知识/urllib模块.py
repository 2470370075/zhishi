from urllib import request          # python2的urllib2
from urllib import parse            # python2的urllib

r = request.urlopen('https://baidu.com/')
print(r.status)
print(r.read())

ua_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
req = request.Request('https://baidu.com/',headers=ua_headers)
r = request.urlopen(req)
print(r.read())


dic = {'a':'知乎'}
d = parse.urlencode(dic)
print(d)
print(parse.unquote(d))