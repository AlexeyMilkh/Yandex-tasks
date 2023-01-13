"""Алгоритм шифрования:
    1. Подсчитывается количество различных символов в ФИО (регистр важен, А и а - разные символы)
    2. Берется сумма цифр в две и месяце рождения, умноженная на 64
    3. Для первой (по позиции в слове) буквы фамилии определяется ее номер в алфавите (в 1-индексации), умноженный на
       256 (регистр буквы не важен)
    4. Полученные числа суммируются
    5. Результат переводится в 16-ричную систему счисления (в верхнем регистре)
    6. У результата сохраняются только 3 младших разряда (если значимых разрядов меньше, то шифр дополняется до 3х
       разрядов ведущими нулями

Задача - вычислить для кандидата его шифр

Формат ввода:
    В первой строке вводится число N(1≤N≤10000) — количество кандидатов и шифров.
    Далее следует N строк в формате CSV (fj,ij,oj,dj,mj,yj) — информация о кандидатах:
    1. Фамилия fj, имя ij и отчество oj(1≤∣∣fj∣∣,∣∣ij∣∣,∣∣oj∣∣≤15) — строки, состоящие из латинских букв верхнего и
       нижнего регистра;
    2. День рождения dj, месяц рождения mj и год рождения yj — целые числа, задающие корректную дату в промежутке от 1
       января 1950 года до 31 декабря 2021 года.

Формат вывода:
    В единственной строке выведите N строк k1, k2, …, kN, где kj — шифр j-го кандидата (в верхнем регистре). Кандидаты
    нумеруются с 1 до N в порядке ввода.

Ввод: input.txt
Вывод: output.txt

Пример:
Ввод:
2
Volozh,Arcady,Yurievich,11,2,1964
Segalovich,Ilya,Valentinovich,13,9,1964
Вывод:
710 64F
"""


alphabet = {'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
            'P': 16,
            'Q': 17,
            'R': 18,
            'S': 19,
            'T': 20,
            'U': 21,
            'V': 22,
            'W': 23,
            'X': 24,
            'Y': 25,
            'Z': 26}
hex_code = '0123456789ABCDEF'

with open("input.txt", "r") as file:
    amount = int(file.readline())

    final = ''
    data = ''
    for i in range(amount):
        data += file.readline()

        name = []
        for j in data:
            if j.isalpha():
                name.append(j)

        first_letter = alphabet[name[0]]

        date_birth = []
        for j in data:
            if j.isdigit():
                date_birth.append(j)

        summa = 0
        for j in range(0, len(date_birth)-4):
            summa += int(date_birth[j])

        unique_name = []
        count = 0
        for j in name:
            if j not in unique_name:
                count += 1
                unique_name.append(j)

        res = len(unique_name) + summa*64 + first_letter*256

        s = ''
        while res > 0:
            s = hex_code[res % 16] + s
            res = res // 16

        if len(s) > 3:
            code = s[-3:]
        else:
            code = s
            while len(code) < 3:
                code += '0'
        print(code)
        data = ''
        final += code + ' '

with open("output.txt", "w") as file:
    file.write(final[:-1])


