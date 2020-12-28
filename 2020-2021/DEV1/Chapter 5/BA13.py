x = 1
divisibleBy = ''

while x <= 10:
    if x % 2 == 0:
        divisibleBy = str(x) + ' is divisible by 2'
    if x % 3 == 0:
        divisibleBy = str(x) + ' is divisible by 3'
    if x % 4 == 0:
        divisibleBy = str(x) + ' is divisible by 4'
    if x % 5 == 0:
        divisibleBy = str(x) + ' is divisible by 5'
    x = x + 1

print()
