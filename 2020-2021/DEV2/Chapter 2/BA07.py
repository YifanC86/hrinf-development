def repeat(n, sym):
  s = ''
  while n > 0:
    s = s + sym
    n = n - 1
  return s

def line(n):
  return repeat(n, '*')

def triangle(n):
  s = ''
  while n > 0 :
    s = line(n) + '\n' + s
    n = n - 1
  return s

ret = repeat(3, '#')
l = line(5)
t = triangle(6)
t2 = triangle(3)
print()