a = int(input())
b = int(input())

a1 = a
b1 = b
while a1 != 0 and b1 != 0:
    if a1 > b1:
        a1 %= b1
    else:
        b1 %= a1
# наибольший общий делитель
nod = a1 + b1
# наименьшее общее кратное
nok = a * b / nod
print(int(a * b / nod))


def nod(a, b):
    a1 = a
    b1 = b
    while a1 != 0 and b1 != 0:
        if a1 > b1:
            a1 %= b1
        else:
            b1 %= a1
    # наибольший общий делитель
    return a1 + b1
