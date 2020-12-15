def sqr(n):
    print()
    return n * n


def sumOfSqr(n):
    ss = 0
    while n > 0:
        ss = ss + sqr(n)
        n = n - 1
    return ss


a = sqr(5)
a = sumOfSqr(5)
a = sumOfSqr(sqr(2))
print()
