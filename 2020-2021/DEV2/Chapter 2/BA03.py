def isDivisible(dividend, divisor):
  return dividend % divisor == 0


def isLeap(year):
  return isDivisible(year, 400) or (isDivisible(year, 4) and not isDivisible(year, 100))

param = 2019
test = isDivisible(param,2)
test = isLeap(param)
print()