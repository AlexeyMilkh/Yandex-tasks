"""Дана строка (возможно, пустая), состоящая из букв A-Z:
AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB

Нужно написать функцию RLE, которая на выходе даст строку вида:
A4B3C2XYZD4E3F3A6B28. И сгенерирует ошибку, если на вход пришла невалидная строка.

* Если символ встречается 1 раз, он остается без изменений. Если символ повторяется больше 1 раза, к нему добавляется
количество повторений"""


def rle(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    last_sym = s[0]
    last_pos = 0
    answer = []
    for i in range(len(s)):
        if s[i] != last_sym:
            answer.append(pack(last_sym, i - last_pos))
            last_pos = i
            last_sym = s[i]
    answer.append(pack(s[last_pos], len(s) - last_pos))
    return ''.join(answer)


print(rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'))
