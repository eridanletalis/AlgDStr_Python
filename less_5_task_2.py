""" Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

# Немного психованный сумматор

numerator = [str(i) for i in range(10)]
numerator = numerator + ['A', 'B', 'C', 'D', 'E', 'F']


def sum(a, b, k=0):
    _iter_a = iter(numerator)
    _iter_b = iter(numerator)
    carrier = 0
    A = next(_iter_a)
    while A != a:
        A = next(_iter_a)
    if k == 1:
        try:
            A = next(_iter_a)
        except StopIteration:
            carrier = 1
            _iter_a = iter(numerator)
            A = next(_iter_a)
    if b != '0':
        while next(_iter_b) != b:
            try:
                A = next(_iter_a)
            except StopIteration:
                carrier = 1
                _iter_a = iter(numerator)
                A = next(_iter_a)

    return A, carrier


def calculate_sum(a, b):
    A = list(a).copy()
    B = list(b).copy()
    A.reverse()
    B.reverse()
    if len(A) > len(B):
        A, B = B, A

    # Делаем сложение. Я сам в шоке от такого алгоритма, но препод требует полёт фанатазии
    i = 0
    k = 0
    s = []
    for i, n in enumerate(A):
        elem, k = sum(n, B[i], k)
        s.append(elem)

    j = i + 1
    while j < len(B):
        elem = B[j]
        if k == 1:
            elem, k = sum(B[j], '0', k)
        s.append(elem)
        j += 1

    if k == 1:
        s.append('1')
    s.reverse()
    return s


# Ещё более прихонутое умножение

def mult_a_on_scalar(a, x):
    sum = ['0']
    _iter_b1 = iter(numerator)
    X = next(_iter_b1)
    while X != x:
        sum = calculate_sum(a, sum)
        X = next(_iter_b1)

    return sum


# тут происходят очень страшные вещи

def multiplicate(a, b):
    A = a.copy()
    B = b.copy()
    mult = ['0']
    part = []
    for i in range(len(A)):
        part = mult_a_on_scalar(B, A[len(A) - 1 - i])
        for j in range(i):
            part.append('0')
        mult = calculate_sum(part, mult)

    return mult


A = list(input("Введите первое  в HEX. Ввод большими буквами и цифрами: "))
B = list(input("Введите второе в HEX. Ввод большими буквамии цифрами: : "))

print(f'Сумма введённых чисел равна {calculate_sum(A, B)}')
print(f'Произведение введённых чисел равно {multiplicate(A, B)}')
