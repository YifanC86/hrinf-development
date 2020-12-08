start = 100
end = 999
print()

num = start
total = 0

while num < end:
    wellOrdered = True
    numberAsString = str(num)
    whileNum = 1
    while whileNum < len(numberAsString) and wellOrdered:
        if int(numberAsString[whileNum - 1]) >= int(numberAsString[whileNum]):
            wellOrdered = False
        whileNum = whileNum + 1
    if wellOrdered:
        total = total + 1
    num = num + 1

print()
