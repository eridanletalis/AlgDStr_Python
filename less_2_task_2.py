"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

print("Введите натуральное число.")
A = int(input())

countOdd = 0
countEven = 0
if A == 0:
    countEven += 1

while A != 0:
    tmp = A // 10
    num = A - tmp * 10
    A = tmp
    if num % 2 != 0:
        countOdd += 1
    else:
        countEven += 1

print(f"В числе {countEven} чётных и {countOdd} нечётных.")
