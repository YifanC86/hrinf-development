number = 9
print()
numberAsBinary = ''
num = number
while num != 0:
    remainder = num % 2
    num = num // 2
    numberAsBinary = str(remainder) + numberAsBinary

print()
