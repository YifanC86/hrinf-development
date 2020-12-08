def breakUp4DigitNumber(num):
  digit4 = num % 10
  num = num // 10
  digit3 = num % 10
  num = num // 10
  digit2 = num % 10
  num = num // 10
  digit1 = num % 10
  num = num // 10
  print()

input = 123
breakUp4DigitNumber(input)