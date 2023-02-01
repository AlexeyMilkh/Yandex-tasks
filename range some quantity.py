"""RSQ - Range Some Quantity"""


def makeprefixsum(nums):  # функция для создания коллекции значений префиксов
    prefixsum = [0] * (len(nums) + 1)  # создаем массив для префиксов на 1 единицу больше исходного
    for i in range(1, len(nums) + 1):  # проходим массив, начиная со второго значения до длины массива + 1
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]  # сумма предыдущего префикса + предыдущее значение равно текущему
    return prefixsum  # возвращаем коллекцию


def rsq(prefixsum, l, r):  # функция для вычисления суммы значений из среза
    return prefixsum[r] - prefixsum[l]  # будет равно разнице значения префиксов на правой и левой границе


print(rsq(makeprefixsum([1, 4, 6, 1, 7, 3, 2, 0]), 2, 8))
