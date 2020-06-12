"""
__new__方法在创建对象时为对象分配内存空间
__init__方法在创建对象时为对象初始化

先运行__new__，返回值传给__init__方法运行

单例模式，一个类只有一个实例
为实现单例模式，重新__new__方法，使每创建的一个对象都是同一个内存空间

实现方法：定义一个类的instance属性，第一次实例化的时候把对象赋值给这个属性，以后每次实例化的时候直接返回这个属性。
"""

class A():

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


a1 = A()
a2 = A()

print(a1)
print(a2)