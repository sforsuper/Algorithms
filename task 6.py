def selection_sort(list):
    for i in range(len(list) - 1):
        minn = list[i]
        a = i
        for j in range(i+1, len(list)):
            if minn > list[j]:
                minn = list[j]
                a = j
        if a != i:
            b = list[i]
            list[i] = list[a]
            list[a] = b
c = list(map(int, input().split()))
selection_sort(c)
print(c)