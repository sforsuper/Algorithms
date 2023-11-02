def shell_sort(list):
    gap = len(list)//2

    while gap > 0:
        for i in range(gap, len(list)):
            current_value = list[i]
            index = i
            while index >= gap and list[index - gap] > current_value:
                list[index] = list[index-gap]
                index -= gap
                list[index] = current_value
        gap //= 2
    return


b = list(map(int, input().split()))
shell_sort(b)
print(b)
