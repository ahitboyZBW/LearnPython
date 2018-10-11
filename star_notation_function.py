# _*_ coding: utf-8 _*_ 
# 介绍python中的星号*的用处，来源《python cookbok》
###### 解压序列赋值给多个变量
p = (4,5)
x,y = p
print(x)
print(y)

data = ['ACM',50,91.1,(200,100,300)]
name,shares,price,(year,mon,day) = data
print(name)
print(shares)
print(price)
print(year)
print(mon)
print(day)

# 这种赋值可以用在任意可迭代对象，而不单单是列表或者元组，也可以是字符串，文件对象，迭代器和生成器
s= 'hello'
a,b,c,d,e = s
print(a)
# 解压一部分时，可以用任意占位符实现
_,shares,price,_ = data
print(shares)

# 如果可迭代对象的元素个数超过变量的个数时，会抛出ValueError，
# 那么怎么才能从可迭代变量中解压出N个元素：*可以解决
# 情况1： 去掉开头和结尾，只要中间，但是不知道中间到底有多少个元素
grade = [1,2,3,4,5,6]
first,*middle,last = grade
print(middle)# middle 一定是列表
# 情况2 星号表达式用在末尾
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)
# 也可以用在开头
# 星号表达式在迭代元素为可变长元组的序列时，非常有用
records = [ ('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4), ]

def do_foo(x, y):

    print('foo', x, y)

def do_bar(s):

    print('bar', s)

for tag, *args in records: 
    if tag == 'foo': 
        do_foo(*args) 
    elif tag == 'bar': 
        do_bar(*args)

# 星号在字符串分割中的应用
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)

# 星号提取之后丢弃掉，不能只用*号，要用*加上一个废弃的名称，例如_或者ign

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_,(*_,year) = record
print(name)
print(year)