side = 5
s = ''
i = 0
while i < side:
    s = s + '*'
    i = i + 1
s = s + '\n'

i = 0
while i < side - 2:
    s = s + '*'
    j = 0
    while j < side - 2:
        s = s + ' '
        j = j + 1
    s = s + '*\n'
    i = i + 1

i = 0
while i < side:
    s = s + '*'
    i = i + 1
s = s + '\n'
print()
