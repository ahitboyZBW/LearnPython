# _*_ coding: utf-8 _*_ 
# 双端队列
# 两端都可插入与弹出
# from collections import deque # collections 库里有deque

# example:这里用list去模拟deque

class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def print(self):
        print(self.items)
d=Deque()

print(d.isEmpty())

d.addRear(4)

d.addRear('dog')

d.addFront('cat')

d.addFront(True)

print(d.size())

print(d.isEmpty())

d.addRear(8.4)

print(d.removeRear())

print(d.removeFront())

d.print()


# example2： 回文子的判断，正读反读都是一样的词，e.g. radar toot madam

from collections import deque 
def palchecker(aString):
    charDeque = deque()
    for ch in aString:
        charDeque.append(ch)
    while len(charDeque)>1:
        if charDeque.pop() == charDeque.popleft():
            continue
        else:
            return False
    
    return True

print(palchecker('asdfgfdsa'))
print(palchecker('asdfgfdse'))
