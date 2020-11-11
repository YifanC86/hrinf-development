start = 20
end = 199
print()

num = start
res = ''

while num < end:
  numberAsString = str(num)
  palindrome = False
  reverse = ''

  i = len(numberAsString) - 1
  while i >= 0:
    reverse = reverse + numberAsString[i]
    i = i - 1
  reverse = int(reverse)
  if reverse == num:
    res = res + str(num) + '\n'
  
  num = num + 1

print()