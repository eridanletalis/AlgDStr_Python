import random

N = 1000


def bubble_sort(array):
    flag = 0
    # iterations = 0
    n = 0
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = 1        # в текущей итерации были изменения
        if flag == 0:           # если никаких изменений не было
            break               # прерываем цикл
        flag = 0
        n += 1
        # iterations +=1          # для подсчёта количества операций
    #return iterations


array = []
for i in range(N):
    array.append(random.randint(-100, 99))

print(array)
#print(bubble_sort(array))
bubble_sort(array)
print(array)