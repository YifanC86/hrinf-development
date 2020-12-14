def repeat(n, sym):
  s = ''
  while n > 0:
    s = s + sym
    n = n - 1
  return s

n = 5
sym = '*'
ret = repeat(n, sym)
print()