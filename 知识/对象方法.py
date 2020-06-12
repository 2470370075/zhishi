
"""
__call__方法
有了__call__方法，代表对象是可调用的，可以加括号运行，运行的就是__call__函数
"""

class A():

    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('123')

a = A('wjx')
a()

print('/////////////////')

class mylist(list):
    def __call__(self, *args, **kwargs):
        print(l)

l = mylist()
l.append(1)
l.append(2)

l()