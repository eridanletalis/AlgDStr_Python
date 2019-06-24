""""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

import collections

d = collections.defaultdict()

n = int(input("Введите количество предприятий: "))

print("Для каждого предприятия вводите название и прибыль одной строкой через пробел. Ввод завершается по ENTER")
print("Например, РогаНеКопыта 12.1 32.4 14.9 42 <ENTER>")
for i in range(1, n + 1):
    print("Введите информацию предприятия %d" % i)
    name, val1, val2, val3, val4 = input().split()
    d[name] = {"val1": float(val1), "val2": float(val2), "val3": float(val3), "val4": float(val4)}
    d[name]["year"] = (float(sum(d[name].values())))

mean = 0.0
for i in d:
    mean += float(d[i]["year"])

mean /= n

print("Эти товарищи выше среднего значения:")
for i in d:
    if d[i]["year"] > mean:
        print(i)

print("Эти товарищи ниже среднего значения:")
for i in d:
    if d[i]["year"] < mean:
        print(i)
