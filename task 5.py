def insertion_sort(list):
    for i in range(1,len(list)):
        value = list[i]
        a = i - 1
        while a >= 0:
            if value < list[a]:
                list[a+1] = list[a] #перенести число из места а вправо на место а+1
                list[a] = value #перенести значение влево на а
                a = a - 1
            else:
                break
b = list(map(int, input().split()))
insertion_sort(b)
print(b)