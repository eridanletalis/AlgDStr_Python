# Попытка реализовать алгоритм Quickselect
# Недореализовано

import random


# реализация алгоритма Quickseleckt
def median_search(array):
    k = len(array)
    if k % 2 == 1:
        return partition(array, int(k / 2))
    return partition(array, int(k // 2) + 1)


def partition(array, k):
    pivot_idx = random.randint(0, len(array) - 1)
    pivot = array[pivot_idx]
    new_list_less = [array[i] for i in range(len(array)) if array[i] <= pivot]
    new_list_great = [array[i] for i in range(len(array)) if array[i] > pivot]
    if k != 1 and len(new_list_less) >= k:
        partition(new_list_less, k)
    elif k != 1 and len(new_list_less) < k:
        partition(new_list_great, k - len(new_list_less))
    elif k == 1 and len(new_list_less) == k:
        return new_list_less[0]
    elif k == 1 and len(new_list_great) == k:
        return new_list_great[0]


m = int(input("Уважаемый идеальный пользователь, введите натуральное число: "))
n = 2 * m + 1
print(f'Ваш массив состоит из {n} случайных чисел:')

array = [random.randrange(-10000, 10000) for _ in range(n)]

print(array)

print(f'Массив имеет медиану {median_search(array)}')
