height = 5
s = ''
i = 0

while i < height:
    j = 0
    while j + i < height - 1:
        s = s + ' '
        j = j + 1
    while j < height + i:
        s = s + '*'
        j = j + 1
    s = s + '\n'
    i = i + 1
print()
