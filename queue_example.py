# _*_ coding: utf-8 _*_ 
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

def hotPotato(namelist,num):
    potato_queue = Queue()
    for iterm in namelist:
        potato_queue.enqueue(iterm)
    
    while potato_queue.size() > 1:# 还剩一个人的时候停止
        for i in range(num):
            potato_queue.enqueue(potato_queue.dequeue()) #少于循环次数时将队头的放到队尾
        potato_queue.dequeue() #删除队尾的倒霉蛋
    return potato_queue.dequeue() #返回最后一个人


    
    


def main():
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q.dequeue())
    print(q)

    print(hotPotato(['A','B','C','D','E','F'],7))
    
if __name__ == '__main__':
   main()
else:
    print('FUCK PYTHON')