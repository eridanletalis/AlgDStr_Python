# Вариант 1. Реализация рекурсии
# Задача выполнена исходя из предположения, что пока функция находится в стеке, её тоже нужно хранить в памяти
# по аналогии с уроком, посмотрим содержимое функции
# b'\x01\x00\x00\x00\x00\x00\x00\x00@\x12\n\xb5\xfd\x7f\x00\x00\x10\xd8\x93\xe8\xe3\x01\x00\x00\xd0\x02\x90\xe8\xe3\
# x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0,
# \n\xb5\xfd\x7f\x00\x00p\xc5r\xea\xe3\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
# \x000\xe9\x92\xe8\xe3\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\xc5r\xea\xe3\x01\x00\x00C\x00:\x00\\\x00P
# \x00r\x00o\x00g\x00r\x00a\x00m\x00 \x00F\x00'
# (1, 0, 3037336128, 32765, 3902003216, 483, 3901752016, 483, 0, 0, 0, 0, 0, 0, 3037342944, 32765, 3933390192,
# 483, 0, 0, 0, 0, 3901942064, 483, 0, 0, 3933390192, 483, 3801155, 5242972, 7274610, 7471207, 7143521, 4587552)
# При N = 10
# Затраты на хранение переменных при  рекурсии: 244 байт.
# Затраты на хранения функции при рекурсии: 1224 байт.
# Суммарно на задачу потрачено 1496 байт.
# При N = 100
# Затраты на хранение переменных при  рекурсии: 2404 байт.
# Затраты на хранения функции при рекурсии: 13464 байт.
# Суммарно на задачу потрачено 15896 байт.
# При N = 1000
# Затраты на хранение переменных при  рекурсии: 24004 байт.
# Затраты на хранения функции при рекурсии: 135864 байт.
# Суммарно на задачу потрачено 159896 байт.
# Очевидно, затраты на вычисления растут линейно как по месту, занимаемому функцию, так и по месту, занимаемому
# переменными


import sys
# import ctypes
# import struct
sys.setrecursionlimit(1060)

N = 1000

# Для рекурсии

def elem_rec(n):
    global space_for_variables
    global space_for_funcions
    if n == 1:
        space_for_variables += sys.getsizeof(n)
        return 1
    elem = 1 / ((-2) ** (n - 1))
    space_for_variables += sys.getsizeof(elem)
    space_for_funcions += sys.getsizeof(elem_rec)
    return elem + elem_rec(n - 1)

space_for_variables = 0
space_for_funcions = 0
print(elem_rec(N))
# print(ctypes.string_at(id(elem_rec), sys.getsizeof(elem_rec)))
# print(struct.unpack('L'*33 + 'l', ctypes.string_at(id(elem_rec), sys.getsizeof(elem_rec))))
print(f'Затраты на хранение переменных при  рекурсии: {space_for_variables} байт.')
print(f'Затраты на хранения функции при рекурсии: {space_for_funcions} байт.' )
print(f'Суммарно на задачу потрачено {space_for_variables + space_for_funcions + sys.getsizeof(N)} байт.')


# Для функции с циклом
# В этой задаче, хотя функция вызывается постоянно, одномоментно в стеке может находиться только один экземпляр
# фунции elem, а также переменные N и s.
# При N = 10
# Затраты на хранение переменных при  цикле: 80 байт.
# Затраты на хранения функции при цикле: 136 байт.
# Суммарно на задачу потрачено 216 байт.
# При N = 100
# Затраты на хранение переменных при  цикле: 80 байт.
# Затраты на хранения функции при цикле: 136 байт.
# Суммарно на задачу потрачено 216 байт.
# При N = 1000
# Затраты на хранение переменных при  цикле: 80 байт.
# Затраты на хранения функции при цикле: 136 байт.
# Суммарно на задачу потрачено 216 байт.
# Как видно, количество байт, затраченных на задачу, констатно. По затратам памяти этот вариант может считаться
# лучше варианта с рекурсией

def elem(n):
    global space_for_variable_max
    s = 1 / ((-2) ** (n - 1))
    # Вдруг при очередной операции нам потребуется большее количество памяти для хранения
    space_for_variable_max = space_for_variable_max if space_for_variable_max > sys.getsizeof(s) else sys.getsizeof(s)
    return s

n = int(N)
space_for_funcions = sys.getsizeof(elem)
space_for_variable_max = 0
s = 1
space_for_variables = sys.getsizeof(s) + sys.getsizeof(n)
while n > 1:
    s += elem(n)
    n -= 1

space_for_variables += space_for_variable_max

print(f'Затраты на хранение переменных при  цикле: {space_for_variables} байт.')
print(f'Затраты на хранения функции при цикле: {space_for_funcions} байт.' )
print(f'Суммарно на задачу потрачено {space_for_variables + space_for_funcions} байт.')


# Для свёрнутого в сумму геометрических прогрессий ряда
# Очевидно, что количество памяти, выделяемое задаче, не будет зависеть от N, поэтому рассчитаем для N = 1000
# Затраты на хранение переменных на задачу: 148 байт.
# Полученное число меньше, чем во всех других вариантах. Если предположить, что считаем только переменные, не
# учитывая функции, то здесь затраты на их хранение сравнимы с затратами цикла, однако, из экспериментов,
# проводимых в задаче 4.1 (файл less4_task_1.py), видно, что "математическое" решение задачи является самым быстрым
# и не зависит от размера N. Таким образом, я остановил бы выбор именно на этой версии

if N % 2 == 0:  # Если количество элементов чётно, просто делим надвое.
   n1 = n2 = N / 2
else:  # иначе, положительных элементов ряда будет больше, чем отрицательных
   n1 = N // 2 + 1
   n2 = N - n1

S1 = 4 * (1 - (1 / 4) ** n1) / 3  # суммируем по положительным элементам
S2 = 2 * (1 - (1 / 4) ** n2) / 3  # суммируем по отрицательным элементам

sum = S1 - S2
space_for_variables = sys.getsizeof(N) + sys.getsizeof(n1) + sys.getsizeof(n2) + sys.getsizeof(S1) + \
    sys.getsizeof(S2) + sys.getsizeof(sum)
print(f'Затраты на хранение переменных на задачу: {space_for_variables} байт.')

