seq = ''
arg = 10
print()
def zero2N(n):
  global seq
  i = 0
  while i < n:
    seq = seq + str(i) + ' '
    i = i + 1
zero2N(arg)
print()