def Unknown(x, y):
    if x < y:
        print(str(x + y))
        return (Unknown(x + 1, y) * 2)
    elif x == y:
        return 1
    else:
        print(str(x + y))
        return (Unknown(x - 1, y) // 2)


def IterativeUnknown(x, y):
    Total = 1
    while x != y:
        print(str(x+y))
        if x < y:
            x = x + 1
            Total = Total * 2
        else:
            x = x - 1
            Total = Total // 2
    return Total



print("10 and 15")
print(str(IterativeUnknown(10, 15)))
print("10 and 10")
print(str(IterativeUnknown(10, 10)))
print("15 and 10")
print(str(IterativeUnknown(15, 10)))
