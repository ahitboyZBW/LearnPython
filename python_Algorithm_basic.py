# _*_ coding: utf-8 _*_ 
"""Python 图解书中的代码"""
"""# 2分查找"""
def binary_search(list,item):
    count = 0
    low = 0
    high = len(list)-1
    while low <= high:
        count += 1
        mid = int((low+high)/2)
        guess = list[mid]
        if guess == item:
            return count,mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid-1
            
    return count,None
# 算法的速度指的不是时间，是随着操作数的增速

# 谈论算法速度的时候，是说随着输入的增多，运行时间以什么样的速度增加
# 访问有两种，一种顺序访问，一种随机访问
#数组支持随机访问
#链表只能顺序访问

""" 选择排序: 先查找序列最小值，放在新序列最前面，再从剩下的序列中查找最小，放在新序列第二位，依次类推；算法复杂度O（n^2） """
def findSmallest(arr):#返回序列最小值位置
    smallest = arr[0]
    smallest_index = 0
    for i in range(0,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectSort(arr):
    newarr = []
    for i in range(0,len(arr)): 
        smallest = findSmallest(arr) #查找最小值位置
        newarr.append(arr.pop(smallest))#放在新数列最后面，并将其从原序列删除
    return newarr

# 栈有两个操作：压入和弹出
# 所有的函数调用都被压入栈
# 调用栈如果太长，将会占用大量内存

# 递归sum
def recursive_sum(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 0:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])

# 递归len for list
def recursive_len(arr):
    if arr == []:
        return 0
    else:
        return 1 + recursive_len(arr[0:-1])

# 递归找最大值
def recursive_max(arr):
    if len(arr) == 0:
        return 0
    
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[-1] < recursive_max(arr[0:-1]):
            return recursive_max(arr[0:-1])
        else:
            return arr[-1]

# 快速排序
def quicksort_v1(arr):
    if len(arr) < 2:
        return arr # 基线条件，当长度为1或者0时返回自身
    else:
        pivot = arr[0] #选取一个元素，最好不要用第一个，随机最好
        less = [i for i in arr[1:] if i <= pivot] #获取比pivot小的数列
        greater = [i for i in arr[1:] if i > pivot] # 获取比pivot大的数列

        return quicksort_v1(less) + [pivot] + quicksort_v1(greater) # 对上下子列排序，在拼在一起

# 二分查找 O(logn) 简单查找O(n)  快速排序 合并排序O(nlogn) 选择排序O(n^2) 旅行商问题 O(n!)

# 散列表，更快的查找（hash table） python 里的dict,由建和值组成
# book = dict()
# book = {} 两种方式一样
# book["apple"] = 0.7
''' 一个服务器缓存的例子
cache = {}
def get_page(url):
    if cache.get(url):
        return catch[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data
'''
# 数组的插入时间复杂度为O(n)

# 数组的读取时间复杂度为O(1)

# 数组的删除时间复杂度为O(n)

# 链表的插入时间复杂度为O(1)

# 链表的读取时间复杂度为O(n)

# 链表的删除时间复杂度为O(1) (注意是删除第一个和最后一个，即立即能访问到的元 素时间复杂度才是1)

#           散列表（平均情况）   散列表（最坏情况）     数组     链表
#    查找      O(1)                  O(n)            O(1)     O(n)
#    插入      O(1)                  O(n)            O(n)     O(1)
#    删除      O(1)                  O(n)            O(n)     O(1) 



# 广度优先搜索 breadth-first search BFS
# 解决最短问题的算法成为广度优先搜索
# 广度优先搜索是图的查找算法，主要回答两个问题
# 第一类问题：从节点A出发，有前往节点B的路径吗？
# 第二类问题：从节点A出发，前往节点B的哪一条路径最短

# 图的构建是通过散列表实现
'''
graph = {}
graph['you'] = ['alice','bob','claire']
graph['bob'] = ['asd',',....']
....

'''

# 广度优先搜索的实现方法是通过队列实现
# 1、构建一个队列用来存储要检查的元素
# 2、从队列弹出一个元素
# 3、这个元素是否是想要的（先判断是不是已经判断过了，避免死循环）
# 4、不是，的话将邻居加入队列，返回2
# 5、是的话结束

'''
from collections import deque
search_queue = deque()
search_queue += graph['you'] ,加入你的邻居
searched = []

while search_queue:   队列不为空
    person = search_queue.popleft()
    if not person in searched:

        if person_is_satified():
            print person is the searching result
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
return False

'''

# 当图的边存在加权时，再去找最短路径需要用Dijkstra‘s algorithm，！！！！！！！！！！！！！只适用于有向无环图，
# 如果有负权边，算法不适用，需要采用Bellman-Ford algorithm
# 算法步骤：1、找出最便宜的节点
#          2、更新该节点邻居的开销：对于该点的邻居，检查是否有前往他们的更短的路径，如果有，就更新其开销
#          3、重复这个过程，直到对图中的每个节点都这么做
#          4、计算最终路径

#具体算法实现
# 只要还有要处理的节点
#获取离起点最近的节点
#更新其邻居的开销
#如果有邻居的开销被更新，同时更新父节点
#将该处理节点标记为处理过
#返回第一步

def main():
    mylist=[1,3,5,7,9]
    print(binary_search(mylist,3))
    print(binary_search(mylist,4))

    mylist=[3,5,5,7,9,1]
    print(selectSort(mylist))# 为什么跑完这一步这个数列就没了？？？？？？？   python都是按引用传参

    print(mylist)
    mylist=[3,5,5,7,9,1]
    print(recursive_sum(mylist))

    mylist=[3,5,5,7,9,1]
    print(recursive_len(mylist))

    mylist=[3,5,5,7,9,1]
    print(recursive_max(mylist))

    mylist=[3,5,5,7,9,1]
    print(quicksort_v1(mylist))

    # Dijkstra example
    # 简历散列表存储图
    graph_Dij = {}# 即要存储邻居也要存储到邻居的权重
    graph_Dij['start']={}
    graph_Dij['start']['a']=6
    graph_Dij['start']['b']=2
    graph_Dij['a']={}
    graph_Dij['a']['final']=1
    graph_Dij['b']={}
    graph_Dij['b']={}
    graph_Dij['b']['a']=3
<<<<<<< HEAD
    graph_Dij['b']['final']=5
=======
    graph_Dij['b']['final'=5
>>>>>>> cd24ca1927c74bdbf29cde83f519121a0945bb20
    graph_Dij['final']={}
    #再用一个散列表存储每个节点的开销
    infinity = float('inf')
    costs = {}
    costs['a']=6
    costs['b']=2
    costs['fin']=infinity
    # 父节点散列表
    parents = {}
    parents['a']='start'
    parents['b']='start'
    parents['fin']=None

    # 需要一个数组存储已经处理过的节点
    processed = []
<<<<<<< HEAD
    
=======
>>>>>>> cd24ca1927c74bdbf29cde83f519121a0945bb20
    
if __name__ == '__main__':
   main()
else:
    print('FUCK PYTHON')