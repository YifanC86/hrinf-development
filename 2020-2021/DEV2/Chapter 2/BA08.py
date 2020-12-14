def repeat(n, sym):
  s = ''
  while n > 0:
    s = s + sym
    n = n - 1
  return s

def line(n):
  l = repeat(n, '*')
  return l

def hollowLine(n):
  l = n - 2
  spaces = repeat(l, ' ')
  s = '*' + spaces + '*'
  return s

def hollowSquare(n):
  l = line(n)
  hl = hollowLine(n)
  r = repeat(n-2, hl + '\n')
  s = l + '\n' + r + l + '\n'
  return s

n = 5
s = hollowSquare(n)
print()