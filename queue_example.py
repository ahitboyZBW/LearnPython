# 利用list创建队列
# 队列的队尾在列表的0位置
class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):#在队列的0位置插入新元素
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)




def main():
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q.dequeue())
    print(q)
    
if __name__ == '__main__':
   main()
else:
    print('FUCK PYTHON')