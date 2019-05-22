"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
"""

print("Приготовьтесь ввести координаты двух точек уравнения прямой.")
print("Каждая координата записывается двумя числами x и y через пробел, ")
print("завершение вывода каждой пары числе - ENTER")

x1, y1 = map(float, input("Введите первую координату: ").split())
x2, y2 = map(float, input("Введите вторую координату: ").split())

print("Ваш ввод: ")
print(f"Первая координата ({x1}, {y1}).")
print(f"Вторая координата ({x2}, {y2}).")

if (x1 == x2) & (y1 == y2):
    print("Вы ввели одну и ту же координату. Построение уравнения невозможно")
else:
    A = (y2 - y1)
    B = (x2 - x1)
    C = (x1 * y2 - x2 * y1)
    if B == 0:
        if A == 0:
            print(f"y = {-C}")
        else:
            print(f"y = {-A}x + {-C}")
    else:
        if A == 0:
            print(f"y = {-C / B}")
        else:
            print(f"{-A / B}x + {-C / B}")
