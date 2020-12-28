x = 0
while x < 12:
    x = x + 1
    if x == 5:
        s = '*** 5 is odd ***'
    elif x % 2 == 0:
        s = f"{x} is even"
    else:
        s = f"{x} is odd"
print()
