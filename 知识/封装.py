# 对象的封装就是 __
# 内部可以使用，外部不能使用

class A():

    __n = 1
    def __init__(self,name):
        self.__name = name

    def __func(self):
        self.__n += 1
        return self.__n

a = A('wjx')
# print(a.__name)       # 以这种形式访问不到
print(a._A__func())      # 以这种形式仍然可以访问到
