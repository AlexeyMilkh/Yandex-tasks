"""Игрок в футбол обладает одной числовой характеристикой - профессионализмом. Команда называется сплочённой, если
профессионализм любого игрока не превосходит суммарный профессионализм любых двух других игроков из команды. Команда
может состоять из любого количества игроков. Дана отсортированная последовательность числен длиной N - профессионализм
игроков.
Необходимо найти максимальный суммарный профессионализм сплочённой команды."""


def bestteamsum(players):
    bestsum = 0  # максимальный суммарный профессионализм
    nowsum = 0  # текущий суммарный профессионализм
    last = 0
    for first in range(len(players)):  # перебираем от самого слабого игрока в команде
        # пока сильный игрок не вылез за количество игроков и, команда не сократилась до одного игрока или
        # суммарный профессионализм двух слабых игроков больше либо равен сильному
        while last < len(players) and (last == first or players[first] + players[first + 1] >= players[last]):
            nowsum += players[last]
            last += 1  # берём в команду следующего сильного игрока
        bestsum = max(bestsum, nowsum)  # выбираем лучшую команду
        nowsum -= players[first]  # убираем самого слабого игрока и текущей команды
    return bestsum


gamers = [1, 1, 3, 3, 5, 6, 12]
print(bestteamsum(gamers))
