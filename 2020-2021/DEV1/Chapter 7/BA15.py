w = 5
h = 6
s = ''
i = 0
while i < w:
  s = s + '='
  i = i + 1
j = 0
s = s + '\n'
while j < h - 2:
  i = 0
  while i < w:
    if i == 0 or i == w - 1:
      s = s + "|"
    else:
      s = s + "*"
    i = i + 1
  s = s +  '\n'
  j = j + 1
i = 0
while i < w:
  s = s + '='
  i = i + 1
print()