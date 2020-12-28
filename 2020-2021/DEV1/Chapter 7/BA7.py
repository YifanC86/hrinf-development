h = 5
s = ''
i = 0
k = h
while i < h:
    j = 0
    while j < k - 1:
        s = s + ' '
        j = j + 1
    k = k - 1
    z = 0
    while z < (i + 1):
        s = s + '*'
        z = z + 1
    s = s + '\n'
    i = i + 1
print()
