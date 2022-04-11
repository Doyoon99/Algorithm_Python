# 24090
import sys
sys.setrecursionlimit(1000000)

global count
count = 0

def quick_sort(a, k):
    quick_sort_sub(a, 0, len(a)-1, k)

def quick_sort_sub(a, start, end, k):
    if start < end:
        num = partition(a, start, end)
        quick_sort_sub(a, start, num-1, k)
        quick_sort_sub(a, num + 1, end, k)

def partition(a, start, end):
    global count
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            count += 1
            if count == k:
                print(array[j], array[i])
            a[i], a[j] = a[j], a[i]
            i += 1
    if i != end:
        count += 1 
        if count == k: 
            print(array[i], array[end])
        a[i], a[end] = a[end], a[i]
    return i

n, k = map(int, input().split())
array = list(map(int, input().split()))    
    
quick_sort(array, k)
if count < k:
    print(-1)
