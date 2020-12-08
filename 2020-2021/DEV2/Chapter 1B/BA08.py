def line(n, c):
    global s
    while n >  0:
        s = s + c
        n = n - 1

s = ''
line(5, '@')

def shape(m, c):
    global s
    i=1
    while i <= m:
        line(i, c)
        s = s +'\n'
        i = i + 1

s = ''
shape(4, '*')
print()