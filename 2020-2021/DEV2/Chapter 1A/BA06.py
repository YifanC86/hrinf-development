n = 1
print()


def oddEven():
    global status
    if n % 2 == 0:
        status = str(n) + ' is Even'
    else:
        status = str(n) + ' is Odd'


status = ''
oddEven()
print()
