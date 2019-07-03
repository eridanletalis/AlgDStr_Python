import random

N = 101

array = [random.uniform(0, 50) if float(_) != float(50) else float(_ - 0.0000001) for _ in range(N)]

# Попытка реализовать Алгоритм М (Кнут, Т.3)
def merge_sort(array):
    if len(array) > 1:          # если есть, что сравнивать. Список из 1го элемента упорядочен по умолчанию

        middle = len(array) // 2    # берём среднее. Если массив не чётный, то левая сторона будет меньше правой,
                                    # Алгоритм M  допускает небольшое отклонения между len(left) и len(right)

        left_half = array[:middle]

        righ_thalf = array[middle:]

        merge_sort(left_half)   # углубляемся влево, разбивая на всё меньшие остатки, пока не будет 1
        merge_sort(righ_thalf)   # и вправо

        i = 0   # индекс для левой части
        j = 0   # индекс для правой части
        k = 0   # индекс для результирующего

        while i < len(left_half) and j < len(righ_thalf): # Пока не достигли конца любой из сторон
            if left_half[i] < righ_thalf[j]:    # сравниваем, если левый элемент меньше правого
                array[k] = left_half[i]         # то записываем левый элемент
                i = i + 1                       # индекс левого увеличиваем
            else:
                array[k] = righ_thalf[j]        # иначе по аналогии, но с правым
                j = j + 1
            k = k + 1

        while i < len(left_half):               # записываем то, что осталось, если осталось
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(righ_thalf):              # записываем то, что осталось, если осталось
            array[k] = righ_thalf[j]
            j = j + 1
            k = k + 1


print(array)

merge_sort(array)


print(array)
