
# _*_ coding: utf-8 _*_ 
"""这个程序包含一些python基本知识，平时看到的都会弄到这里，是可以直接执行的代码"""
# reference http://cs231n.github.io/python-numpy-tutorial/
# python cookbook

"""经典的hello world"""
print('Hello world')
"""基本的数据类型"""

# number 
# 没有x++和x--运算符
x = 3
print(type(x)) # Prints "<class 'int'>"
print(x)       # Prints "3"
print(x + 1)   # Addition; prints "4"
print(x - 1)   # Subtraction; prints "2"
print(x * 2)   # Multiplication; prints "6"
print(x ** 2)  # Exponentiation; prints "9"
x += 1
print(x)  # Prints "4"
x *= 2
print(x)  # Prints "8"
y = 2.5
print(type(y)) # Prints "<class 'float'>"
print(y, y + 1, y * 2, y ** 2) # Prints "2.5 3.5 5.0 6.25"

#-- 寻求帮助:
    #dir(obj)            # 简单的列出对象obj所包含的方法名称，返回一个字符串列表
#dir(list)
    #help(obj.func)      # 查询obj.func的具体介绍和用法
#help(list.pop)
#-- 测试类型的三种方法，推荐第三种
L=[1,2,3]
if type(L) == type([]):
    print("L is list")
if type(L) == list:
    print("L is list")
if isinstance(L, list):
    print("L is list")
