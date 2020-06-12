
# sorted（）相当于for i in 括号里的参数，把i排序，key=相当于把i加工一下,按加工之后的排序，但是最后排序结果还是原来的i
# 结果里面只有排序好的i
# sort和sorted一样，只是sorted返回新的列表，sort排序原来的对象

# 按照键排序
l3 = sorted({1: 'D', 5: 'B', 2: 'B', 4: 'E', 3: 'A'}.items(),key = lambda item:item[0])
print('l3',l3)

l2 = sorted([1,5,3,2],key=lambda item:item**2)
l4 = sorted([1,5,3,2],reverse=True)

l1 = sorted({1: 'D', 5: 'B', 2: 'B', 4: 'E', 3: 'A'})
l5 = sorted({1: 'D', 5: 'B', 2: 'B', 4: 'E', 3: 'A'}.values(),key=lambda x:x.lower())
l6 = sorted(['b','a','c','A','C','B'],key=lambda item:item.lower())
l7 = sorted(['b','a','c','A','C','B'],key=str.lower)         # 不懂

print(l7)


l = ['b','a','c','A','C','B']
l.sort(key=lambda item:item.upper(),reverse=True)
print(l)