def line(n, c):
  global s
  while n > 0:
    s = s + c
    n = n - 1

s = ''
line(5, '@')
s = ''
line(1, '1')
s = s + '\n'
line(2, '2')
s = s + '\n'
line(3, '3')
print()