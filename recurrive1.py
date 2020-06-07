def fact(n):
    if n == 1:
        return 1

    x = n * fact(n-1)
    print(x)
    return x


print(fact(3))
