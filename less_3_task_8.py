"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

print("Матрица заполняется поэлементно. Завершайте ввод каждого числа клавишей ENTER")

matrix = []
for i in range(5):
    if i != 4:
        matrix.append([])
        print(f"Заполняем строку {i + 1}")
        for j in range(4):
            matrix[i].append(float(input()))
        print(f"Ввод строки {i + 1} завершён")
    else:
        matrix.append([0] * 4)
        print("Ручной ввод завершён, начинаем вычисления")
        for i in range(matrix.__len__() - 1):
            for j in range(matrix[i].__len__()):
                matrix[4][j] += matrix[i][j]
        print("Вычисления завершены")

print("Результирующая матрица:")
for i in range(matrix.__len__()):
    print()
    for j in range(matrix[i].__len__()):
        print("{:5}".format(matrix[i][j]), end="\t")
