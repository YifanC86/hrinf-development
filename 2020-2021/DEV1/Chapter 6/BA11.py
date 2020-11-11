base = 5
fig = ''
i = 1

while i <= base:
  j = 1
  while j <= base + 1 - i:
    fig = fig + str(base + 1 - j)
    j = j + 1
  fig = fig + '\n'
  i = i + 1

print()