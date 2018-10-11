# _*_ coding: utf-8 _*_ 
# Python 中Zip 函数的用法
""" 官方的注释
Help on built-in function zip in module __builtin__:

zip(...)
    zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]

    Return a list of tuples, where each tuple contains the i-th element
    from each of the argument sequences.  The returned list is truncated
    in length to the length of the shortest argument sequence.
None
定义：zip([seql, …])接受一系列可迭代对象作为参数，
将对象中对应的元素打包成一个个tuple（元组），
然后返回由这些tuples组成的list（列表）。
传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。

 """
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

xyz = zip(x, y, z)

print(list(xyz))

'''结果是:'''
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


# 无参数是
""" x = zip()
print(x) """

x2, y2 = zip(*zip(x, y))

print(x == list(x2), y==list(y2))
#---------------------------------------#

#长度不等时，取长度的最小的

x = [1, 2, 3]
y = ['a', 'b', 'c', 'd']
xy = zip(x, y)
print(list(xy))

#结果是：
#[(1, 'a'), (2, 'b'), (3, 'c')]


#--------------------------------------#

#可变参数传递的使用(很常用一种用法)，这个可以用矩阵的转置o~如下：实验
#楼的那代码就是转置矩阵

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]
y = zip(*x)


#结果是：
#[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

#转置就是：
print(list(map(list,y) ))


#这种也经常这样使用: 压缩与解压缩

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

xyz = zip(x, y, z)
res = zip(*xyz)
print(list(res))

#结果可想而知， 压缩之后 在解压缩:
#[(1, 2, 3), (4, 5, 6), (7, 8, 9)]

''''''

#还有就是字典的构造也经常使用：

x = ['a', 'b', 'c']
y = ['x', 'y', 'z']
z = zip(x, y)
d = dict(z)
print(d)

#结果为:
#{'a': 'x', 'c': 'z', 'b': 'y'}

''''''
#------------------------------#
#与iter合用：

a = [1, 2, 3, 4, 5, 6]
b = zip(*([iter(a)] * 2))
print(list(b))

#结果是：
#[(1, 2), (3, 4), (5, 6)]


#https://blog.csdn.net/shomy_liu/article/details/46968651?utm_source=copy 
