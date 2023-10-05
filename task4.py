# bubble_sort для сортировки по убыванию
def swap(list, num1, num2):
    list[num1], list[num2] = list[num2], list[num1]


def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] < a[j + 1]:
                swap(a, j, j + 1)

''' Случай, когда обменов нет. Для него используем оптимизацию... '''
def opt_bubble_sort(list):
    i = 0
    t = True
    while t:
        t = False
        for j in range(len(list) - 1 - i):
            if list[j] < list[j + 1]:
                swap(list, j, j + 1)
                t = True
        i += 1



a = list(map(int, input().split()))
b = list(map(int, input().split()))

bubble_sort(a)
opt_bubble_sort(b)
print(a)
print(b)
