"""
6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за
10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.
"""

from random import randint


def moreLess(a, b):
    if a > b:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
    return 0


a = randint(0, 101)
print("Загадано случайное целое число от 0 до 100. Вам необходимо его отгадать")
myCnt = 10
correct = False

while myCnt > 0 and not correct:
    print(f"Ваша попытка номер {11 - myCnt}:")
    b = int(input())
    if a == b:
        correct = True
    else:
        print("Неверно.")
        myCnt -= 1
        moreLess(a, b)

if correct:
    print("Вы угадали верно!")
else:
    print(f"У вас закончились попытки. Загадано {a}")
