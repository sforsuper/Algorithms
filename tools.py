

def min_index(list, start):
    mn = list[start]
    mn_index = start
    for i in range(start + 1, len(list)):
        if list[i] < mn:
            mn = list[i]
            mn_index = i
    return mn_index
