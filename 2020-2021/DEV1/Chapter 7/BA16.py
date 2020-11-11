size = 5
s = ''
row = 0

while row < size:
  col = 0
  if row == 0 or row == size - 1:
    while col < size:
      s = s + '+'
      col = col + 1
  else:
    while col<size:
      if col == 0 or col == size - 1:
        s = s + '+'
      elif col <= row:
        s = s + '='
      else:
        s = s + '#'
      col = col + 1
  row = row + 1
  s = s + '\n'
print()