h = 5
s = ''
i = 0
while i <= h / 2:
    j = 0
    while j < i + 1:
        s = s + '*'
        j = j + 1
    s = s + '\n'
    i = i + 1
while i < h:
    j = 0
    while j < h - i:
        s = s + '*'
        j = j + 1
    s = s + '\n'
    i = i + 1
print()
