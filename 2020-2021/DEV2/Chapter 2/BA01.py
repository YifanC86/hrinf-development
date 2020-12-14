def  diff(a, b):
  d = a - b
  if d < 0:
    d  = d * -1
  return d

x = 9
y = 3
z = diff(x, y)
print()