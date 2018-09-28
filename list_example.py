# _*_ coding: utf-8 _*_ 
# 列表 list，在python中list是一种内置的数据结构，但是其他语言中通常不是，因此这里去构建一个list
# 列表是一些元素的集合，每个元素拥有一个与其它元素不同的相对位置。更具体地说，我们把这种类型的列表称为一个无序列表。
# 我们可以认为列表有第一项、第二项、第三项……也可以索引 到列表的开始（第一项）或列表的最后（最后一项）。为简单起见，我们假设列表不能包含重复项。

# 为了实现无序列表，需要创建一个链表,无序列表是由节点组成的集合
# 先构造节点
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newData):
        self.data = newData
    def setNext(self,newNext):
        self.next = newNext

class UnorderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head) 
        self.head = temp
    def size(self): # 链表求元素个数，查找，删除元素都要用到遍历，终止条件就是当前的引用不为空
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self,item):
        #这个好好想想
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
    
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext)
    def append(self,item): # 算法复杂度为O(n)的实现，采用遍历
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        temp = Node(item)
        current.setNext(temp)
    def appendSimple(self, item):# 算法复杂度为O(1)的实现？？？？
        #tip将你的算法的时间复杂度简化为 O（1）。注 意！这时你需要考虑非常多的特殊情况，同时要修改 add 方法。
        return True # 不会啊



temp = Node(93)
print(temp.getData())
