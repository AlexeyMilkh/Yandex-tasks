"""Мультимножество - это множество, в котором каждый элемент может входить несколько раз.
Это происходит потому, что, добавляя элемент, мы не проверяем, был он уже в этом множестве или нет."""


setsize = 10
myset = [[] for _ in range(setsize)]


def add(x):
    myset[x % setsize].append(x)  # if not find(x): - если мы хотим сделать обычное множество


def find(x):
    for now in myset[x % setsize]:
        if now == x:
            return True
        return False


def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return


add(7)
add(2)
add(22)
add(4)
find(7)
print(myset)
print(find(7))
delete(2)
print(myset)
