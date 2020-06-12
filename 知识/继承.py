# 继承的目的，减少重复代码

# 继承顺序：遵循mro表，从左到右广度优先
class A():

    def __init__(self,name):
        self.name = name

    def run(self):
        print('run')


class B(A):
    def __init__(self,name,age):
        # super就是父类的意思，下面一行代码相当于在代码的中间调用一下父类的函数
        super(B,self).__init__(name)  # python2中需要在括号里写上自己的类名和self
        super().__init__(name)      # python3中不需要在括号里写上自己的类名和self
        self.age=age

b = B('wjx',22)

print(b.name)
print(b.age)