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

temp = Node(93)
print(temp.getData())
