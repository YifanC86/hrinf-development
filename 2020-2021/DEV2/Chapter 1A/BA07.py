def line():
    global i, s
    while i > 0:
        s = s + '*'
        i = i - 1


s = ''
n = 1
while n < 5:
    i = n
    line()
    s = s + '\n'
    n = n + 1
print()
