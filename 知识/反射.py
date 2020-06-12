# 反射就是hasattr(),getattr(),setattr(),delattr()四个方法
# 反射的意思可能就是 用字符串反射类的属性或方法

class A():
    x = 1

    def __init__(self,name):
        self.name = name

    def a(self):
        print(1)

a = A('wjx')
print(hasattr(a,'name'))
print(hasattr(a,'a'))
print(hasattr(a,'b'))

print(getattr(a,'a'))
fun = getattr(a,'a')
fun()
print(getattr(a,'b','默认值'))

setattr(a,'name','jxw')
print(a.name)

delattr(a,'name')
print(hasattr(a,'name'))