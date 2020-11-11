size = 4
print()

fig = ''
i = 1
while i <= size:
  j = 1
  while j <= size:
    if j == i:
      fig = fig + '#'
    else:
      fig = fig + str(j)
    j = j + 1
  fig = fig + '\n' 
  i = i + 1

print()