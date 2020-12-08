number1 = 10
number2 = 40

if number1 < number2:
    smallestNumber = number1
else:
    smallestNumber = number2

n = 1
gcd = 1
while n <= smallestNumber:
    if number1 % n == 0 and number2 % n == 0:
        gcd = n
    n = n + 1

print()
