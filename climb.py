def climb_stairs(n):
    if n <= 1:
        return 1

    a = 1
    b = 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b

print(climb_stairs(4))