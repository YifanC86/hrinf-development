size = 5

timestable = '  |'
j = 1
while j <= size:
  timestable = timestable + '  ' + str(j)
  j = j + 1
timestable = timestable + '\n'

timestable = timestable + '--+---------------\n'
i = 1
while i <= size:
  timestable = timestable + str(i) + ' |'
  j = 1
  while j <= size:
    times = i * j
    if len(str(times)) == 1:
      timestable = timestable + '  '
    else:
      timestable = timestable + ' '
    timestable = timestable + str(times)
    j = j + 1
  timestable = timestable + '\n'
  i = i + 1

print()