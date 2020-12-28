height = 3
s = ''
row = 0
temp = height

while row < height:
    col = 0
    while col < temp - 1:
        s = s + ' '
        col = col + 1
    while col < height + row:
        s = s + '*'
        col = col + 1
    while col - height < height - 1:
        s = s + ' '
        col = col + 1
    s = s + '\n'
    row = row + 1
    temp = temp - 1
print()
