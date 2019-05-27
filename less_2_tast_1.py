"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве
знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об
ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
"""

print("Ввелите знак операции и числа для обработки в формате: ")
print("<операция> <число А> <Число B>,")
print("например: + 10 20")
print("Для выхода из программы введите число 0 не вводя другие числа")

op = -1

while op != '0':
    in_ = input("Ваш ввод: ")
    try:
        op, a, b = in_.split()
    except:
            op = in_
            a = b = "0"
            continue
    finally:
        a = float(a)
        b = float(b)
    if op in ("+","-","*","/"):
        if op == "+":
            print(f"Результат равен {a + b}")
            continue
        if op == "-":
            print(f"Результат равен {a - b}")
            continue
        if op == "*":
            print(f"Результат равен {a * b}")
            continue
        if b == float(0):
            print("На ноль делить нельзя")
            continue
        else:
            print(f"Результат равен {a / b}")
            continue
    else:
         print("Введён не верный знак. Повторите ввод")