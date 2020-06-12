from 知识 import settings

# 类方法，给类用，
# 实际上实现了类的第二种创建方法，实现了从settings中读取
# 但简单来看并没有意义，因为conn3的创建形式也可以满足
# 真正的意义是 实现了创建对象时的代码统一：Mysql.form_conf()


class Mysql():

    def __init__(self,host,port):
        self.host = host
        self.port = port

    @classmethod
    def form_conf(cls):
        return cls(settings.host,settings.port)

    def run(self):
        print(1)

conn1 = Mysql('127.0.0.1','3309')
conn2 = Mysql.form_conf()
conn3 = Mysql(settings.host,settings.port)


print(conn1.host)
print(conn2.host)
print(conn3.host)


