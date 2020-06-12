# 装饰器关键点：func=wrapper

# 最简单的装饰器，实现思路：运用闭包函数，重新定义func,令func等于warpper
def new_function(func):
    f = func
    def wrapper():
        print('start')
        f()
    return wrapper

def func():
    print(1)

func = new_function(func)  # new_function(func)的返回值是wrapper，wrapper里既有原来的func功能，又有其他功能

func()


# 进行优化：
def new_function(func):
    def wrapper():
        print('start')
        func()                # 优化一下，将上面的赋值直接运行，
    return wrapper

@new_function      # 将func = new_function(func)优化成这样
def func():
    print(1)


func()


# 再次优化之后：
def new_function(func):
    def wrapper(*args,**kwargs):   # 考虑到被装饰函数有时需要传参有时不需要，得这么写
        print('start')
        res = func(*args,**kwargs)    # 对于有返回值的被装饰函数，得把返回值拿到，并作为wapper的返回值，才能实现把老的func返回值传递给新的func返回值
        return res
    return wrapper


@new_function
def func(x):
    print(x)
    return 123

res = func('xxxx')
print(res)


# 终极优化：
def deco(name):
    def new_function(func):
        def wrapper(*args,**kwargs):
            print('start')
            print(name)
            res = func(*args,**kwargs)
            return res
        return wrapper
    return new_function


@deco('wjx')             # 使用最外面的deco装饰器，这里可以往里面传参
def func(x):
    print(x)
    return 123

res = func('xxxx')
print(res)

print('/////////////////')


# 实现了一个认证和任意传参的装饰器例子
def deco(para):
    def auth(func):
        def wrapper(*args,**kwargs):
            print('你传入了个{}'.format(para))
            passward = input('请输入密码：')
            if passward == 'saber2014':
                res = func(*args,**kwargs)
            else:
                print('密码错误')
                res = None
            return res
        return wrapper
    return auth

@deco('jb')
def welcome(name):
    print('welcome {}!!!'.format(name))
    return name


print(welcome('wjx'))