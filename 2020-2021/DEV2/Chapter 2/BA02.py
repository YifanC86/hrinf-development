def countup(n):
  if n <= 0:
    return ''
  elif n == 1:
    return '1'
  else:
    return countup(n-1) + ',' + str(n)

a = countup(0)
b = countup(5)
print()