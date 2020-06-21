# 冒泡排序

def maopao(array):
    length = len(array)
    maxlen = length - 1 # 获取数列的最高索引

    while maxlen:# 最少要循环maxlen个大循环
        for i in range(0,maxlen):# 索引从0开始，最高为maxlen
            if array[i] > array[i + 1]:# 比较互换
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
        maxlen -= 1# 获得本轮最大的数后需比较数减1
    return array

# print(maopao([33,445,6578,1,35,548,3436,46]))

def quicksort(array,low,high):
    if low < high:
        q = partition(array,low,high)
        quicksort(array,low,q - 1)
        quicksort(array,q + 1,high)

def partition(array,low,high):
    x = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] <= x:
            i += 1
            array[i],array[j] = array[j],array[i]
    array[i + 1] , array[high] = array[high] , array[i + 1]
    return i + 1

def selectsort(array):
    for i in range(0,len(array)):
        minnum = i # 设置初始最小值
        for j in range(i + 1,len(array)):
            if array[j] < array[minnum]: # 比较得出本轮最小值
                minnum = j

        array[minnum],array[i] = array[i],array[minnum] # 交换到列表前面

if __name__ == '__main__':
    import time
    import numpy as np
    start = time.time()
    lis = list(np.random.random_integers(1000000,size=1000000))
    #quicksort(lis,0,len(lis)-1)
    #maopao(lis)
    list.sort(lis)
    print(lis,f'耗时:{time.time()-start}')




















