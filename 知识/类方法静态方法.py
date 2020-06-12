class A():
    def __init__(self,name):
        self.name = name

    @classmethod                              # 类方法 类能用 对象能用
    def a(cls):
        print(1)

    @staticmethod                             # 静态方法， 都能用
    def b():
        print(2)

    def c(self):                             # 绑定方法，类用不了
        print(3)



ins = A('wjx')
ins.a()



