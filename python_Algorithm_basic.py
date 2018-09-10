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

# 数组的插入时间复杂度为O(n)

# 数组的读取时间复杂度为O(1)

# 数组的删除时间复杂度为O(n)

# 链表的插入时间复杂度为O(1)

# 链表的读取时间复杂度为O(n)

# 链表的删除时间复杂度为O(1) (注意是删除第一个和最后一个，即立即能访问到的元 素时间复杂度才是1)

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



def main():
    mylist=[1,3,5,7,9]
    print(binary_search(mylist,3))
    print(binary_search(mylist,4))

    mylist=[3,5,5,7,9,1]
    print(selectSort(mylist))

if __name__ == '__main__':
   main()
else:
    print('FUCK PYTHON')