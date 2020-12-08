arg = 123
print()
def split(x):
  global s  
  s = ''
  while x > 0:
    s = str(x % 10) + ' ' + s
    x = x // 10
s = ''
split(arg)
print()