"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

# сначала создадим масив, элементами которого являются случайные числа
# LEN управляет количеством элементов массива
# NEGATIVES = 1 говорит о том, что разрешена генерация отрицательных чисел, иначе 0
# AMP управляет размахом чисел относительно своего среднего значения

import random

LEN = 10
NEGATIVES = 1
AMP = 100
A = [random.randint(-AMP / 2 if NEGATIVES else 0, AMP / 2 if NEGATIVES else AMP) for i in range(LEN)]

max_index = 0
min_index = 0

print(f'Before: {A}')

for i in range(A.__len__()):
    if A[i] > A[max_index]:
        max_index = i
    if A[i] < A[min_index]:
        min_index = i

(A[max_index], A[min_index]) = (A[min_index], A[max_index])

print(f'After: {A}')
