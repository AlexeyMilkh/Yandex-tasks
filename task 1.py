"""Дана последовательность чисел длиной N и M запросов.
Запросы: Сколько нулей на полуинтервале [L, R).

Решение: Для каждого префикса посчитаем количество нулей на нём (prefixzeroes). Тогда ответ на запрос на полуинтервале
[L, R): prefixzeroes[R] - prefixzeroes[L]"""


def makeprefixzeroes(nums):  # функция для создания коллекции префиксов (по нулям)
    prefixzeroes = [0] * (len(nums) + 1)  # массив нулей на 1 больше исходного
    for i in range(1, len(nums) + 1):  # проходимся по длине исходного массива со второй позиции + 1
        if nums[i - 1] == 0:  # если предыдущее значение было 0, текущий префикс равен предыдущему + 1
            prefixzeroes[i] = prefixzeroes[i - 1] + 1
        else:  # иначе оставляем прежнее значение
            prefixzeroes[i] = prefixzeroes[i - 1]
    return prefixzeroes  # возвращаем массив


def countzeroes(prefixzeroes, l, r):  # передаем массив префиксов по нулю и границы
    return prefixzeroes[r] - prefixzeroes[l]  # исходное значение будет разницей сумм правой и левой границ


print(countzeroes(makeprefixzeroes([1, 9, 7, 4, 0, 6, 2, 0, 6, 3, 3, 1]), 3, 6))

