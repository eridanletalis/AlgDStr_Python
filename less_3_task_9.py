"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

# сначала создадим масив, элементами которого являются случайные числа
# LEN_X управляет количеством столбцов массива
# LEN_Y управляет количеством строк массива
# NEGATIVES = 1 говорит о том, что разрешена генерация отрицательных чисел, иначе 0
# AMP управляет размахом чисел относительно своего среднего значения

import random

LEN_X = 10
LEN_Y = 10
NEGATIVES = 1
AMP = 100

matrix = []
for i in range(LEN_Y):
    A = [random.randint(-AMP/2 if NEGATIVES else 0, AMP/2 if NEGATIVES else AMP) for i in range(LEN_X)]
    matrix.append(A)

for i in range(LEN_X):
    max_elem = - AMP / 2
    for j in range(LEN_Y):
        if matrix[j][i] < 0 and matrix[j][i] > max_elem:
            max_elem = matrix[j][i]
    print(f"Максимальный отрицательный элемент столбца {i} равен {max_elem}")


for i in range(matrix.__len__()):
    print()
    for j in range(matrix[i].__len__()):
        print("{:5}".format(matrix[i][j]), end="\t")


