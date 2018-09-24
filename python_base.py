
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

# booleans布尔代数 && || not
t = True
f = False
print(type(t)) # Prints "<class 'bool'>"
print(t and f) # Logical AND; prints "False"
print(t or f)  # Logical OR; prints "True"
print(not t)   # Logical NOT; prints "False"
print(t != f)  # Logical XOR; prints "True"

# string 字符串
hello = 'hello'    # String literals can use single quotes
world = "world"    # or double quotes; it does not matter.
print(hello)       # Prints "hello"
print(len(hello))  # String length; prints "5"
hw = hello + ' ' + world  # String concatenation
print(hw)  # prints "hello world"
hw12 = '%s %s %d' % (hello, world, 12)  # sprintf style string formatting
print(hw12)  # prints "hello world 12"

# string 是一个类，有很多成员函数 详情可见 https://docs.python.org/3.5/library/stdtypes.html#string-methods
s = "hello"
print(s.capitalize())  # Capitalize a string; prints "Hello"
print(s.upper())       # Convert a string to uppercase; prints "HELLO"
print(s.rjust(7))      # Right-justify a string, padding with spaces; prints "  hello"
print(s.center(7))     # Center a string, padding with spaces; prints " hello "
print(s.replace('l', '(ell)'))  # Replace all instances of one substring with another;
                                # prints "he(ell)(ell)o"
print('  world '.strip())  # Strip leading and trailing whitespace; prints "world"

""" 容器 containers"""
# list
xs = [3, 1, 2]    # Create a list
print(xs, xs[2])  # Prints "[3, 1, 2] 2"
print(xs[-1])     # Negative indices count from the end of the list; prints "2"
xs[2] = 'foo'     # Lists can contain elements of different types
print(xs)         # Prints "[3, 1, 'foo']"
xs.append('bar')  # Add a new element to the end of the list
print(xs)         # Prints "[3, 1, 'foo', 'bar']"
x = xs.pop()      # Remove and return the last element of the list
print(x, xs)      # Prints "bar [3, 1, 'foo']"

# 像堆栈一样使用list，堆栈是last in first out, 用list的尾作为堆栈的头，append相当于push，pop相当于pop
stack = [3,4,5]
stack.append(6)
print(stack)
print(stack.pop())
print(stack)

# 像队列一下使用list，first in first out,对于list来说，在队尾插入效率并不高，insert之后所有的元素都要向后移动一个。
# 为了更高效率的实现，使用collections.deque，能实现队尾和队头的快速插入和删除

from collections import deque

queue = deque(["Erric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
queue.popleft()
print(queue)

# slicing 操作2：4 = 2，3 不包含最后一个数
nums = list(range(5))     # range is a built-in function that creates a list of integers
print(nums)               # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])          # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])           # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print(nums[:2])           # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])            # Get a slice of the whole list; prints "[0, 1, 2, 3, 4]"
print(nums[:-1])          # Slice indices can be negative; prints "[0, 1, 2, 3]"
nums[2:4] = [8, 9]        # Assign a new sublist to a slice
print(nums)               # Prints "[0, 1, 8, 9, 4]"

animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
# Prints "cat", "dog", "monkey", each on its own line.

# If you want access to the index of each element within the body of a loop, use the built-in enumerate function:
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))

# list comprehensions
# 源代码
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)   # Prints [0, 1, 4, 9, 16]

# 改进的代码
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)   # Prints [0, 1, 4, 9, 16]

nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)  # Prints "[0, 4, 16]"


# Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line
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
