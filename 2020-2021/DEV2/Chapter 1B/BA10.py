def ones(p):
  global s
  if p == 1:
      s =  'one'
  elif p == 2:
      s =  'two'
  elif p == 3:
      s =  'three'
  elif p == 4:
      s =  'four'
  elif p == 5:
      s =  'five'
  elif p == 6:
      s =  'six'
  elif p == 7:
      s =  'seven'
  elif p == 8:
      s =  'eight'
  elif p == 9:
      s =  'nine'

n = 9
s = ''
while n > 0:
  ones(n)
  n = n - 1
print()