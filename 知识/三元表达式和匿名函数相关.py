
# 三元表达式
a = 1
b = 2
h = 1 if a > b else 2
print(h)

print('/////////////////////////')


l = [i**2 if i > 2 else i for i in range(5) ]
print(l)

l = [i**2 for i in range(5) if i > 2]
print(l)

l = (i**2 for i in range(5))      # 中括号变小括号就成生成器了
print(type(l))

p = lambda i:i if i>3 else 0
print(p(2))



print('/////////////////////////')

# map函数，接受两个参数，（一个函数，一个可迭代对象）
# map函数将第二个参数迭代，每一个值传给第一个函数，返回值作为新的列表
l = [1,2,3,4,5]
new = list(map(lambda item:(item % 2 == 0),l))
print('new',new)

l2 = []
for i in l:
    l2.append((i % 2 == 0))
print(l2)

# reduce函数，接受两个参数，（一个函数，一个可迭代对象）
# 将第二个参数迭代，前两个返回值传给第一个函数，得到的返回值再和下一个返回值传给第一个函数，返回最后的返回值
from functools import reduce
f = reduce(lambda a,b:a + b,l)
print('f',f)

# filter函数，接受两个参数，（一个函数，一个可迭代对象）
# 将第二个参数迭代,传给第一个函数，返回值是True就加入新列表
l = [1,2,3,4,5,6,4,5,7,8,9]
l2 = list(filter(lambda x:x%2==1,l))
print(l2)