def repeat(n, sym):
  s = ''
  while n > 0:
    s = s + sym
    n = n - 1
  return s

def line(n):
  return repeat(n, '*')

outcome = line(5)
outcome = line(10)
print()