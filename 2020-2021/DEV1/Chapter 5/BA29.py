n = 20
print()

def fibonacci(n):
  a = 0
  b = 1
  for i in range(0, n):
    temp = a
    a = b
    b = temp + b
  return a
output = ''
l = []
for c in range(0, n):
  output = f"{output}{fibonacci(c)} "
  l.append(fibonacci(c))

average = sum(l) / len(l)

print()