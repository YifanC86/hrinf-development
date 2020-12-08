side = 3
print()
i = side
fig = ''
while i > 0:
    j = 1
    while j <= side:
        fig = fig + str(side + 1 - j)
        j = j + 1
    fig = fig + '\n'
    i = i - 1

print()
