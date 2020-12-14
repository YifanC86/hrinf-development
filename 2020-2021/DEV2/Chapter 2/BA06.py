def repeat(n, sym):
  print()
  s = ''
  while n > 0:
    s = s + sym
    n = n - 1
  return s

def line(n):
  return repeat(n, '*')

def square(n):
  return repeat(n, line(n) + '\n')

def rectangle(width, height):
  return repeat(height, line(width) + '\n')

s = square(5) 
r = rectangle(5, 3)
print()