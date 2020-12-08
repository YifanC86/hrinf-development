number1 = 6
number2 = 10
print()

if number1 > number2:
    maximum = number1
else:
    maximum = number2

lcm = maximum
while not (lcm % number1 == 0 and lcm % number2 == 0):
    lcm = lcm + maximum

print()
