"""Дана отсортированная последовательность чисел длиной N и число K.
Необходимо найти количество пар чисел A, B, таких что B - A > K.

Решение: Возьмём наименьшее число и найдём для него первое подходящее большее. Все ещё большие числа точно подходят.
Возьмём в качестве меньшего числа следующее, а указатель первого подходящего большего будем двигать начиная с той
позиции, где он находится сейчас."""


def cntpairswithdiffgtk(sortednums, k):  # передаём в функцию отсортированный массив и число k
    cntpairs = 0  # в переменной-счетчике храним количество подходящих пар чисел
    last = 0  # правый указатель
    for first in range(len(sortednums)):  # левый указатель двигается, начиная с наименьшего числа
        # проверяем, что мы не вышли за пределы последовательности и на позиции last стоит не подходящее число
        while last < len(sortednums) and sortednums[last] - sortednums[first] <= k:
            last += 1  # двигаем вперёд на одну позицию last
        cntpairs += len(sortednums) - last  # в переменную-счётчик кладем длину оставшегося хвоста
    return cntpairs


data = [1, 4, 6, 5]
print(cntpairswithdiffgtk(data, 4))
