def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    g1 = a[:mid] # 배열1
    g2 = a[mid:] # 배열2
    merge_sort(g1) # 정렬
    merge_sort(g2) # 정렬
    i1 = 0
    i2 = 0
    ia = 0

    while i1 < len(g1) and i2 < len(g2): # 두 배열 비교
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1

    while i1 < len(g1): # 비교 끝난 마지막 배열 처리
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    
    while i2 < len(g2): # 비교 끝난 마지막 배열 처리
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)
