number = 786
print()
inputNumberAsString = str(number)
digitSum = 0
i = len(inputNumberAsString) - 1
while i >= 0:
    digitSum = digitSum + int(inputNumberAsString[i])
    i = i - 1

print()
