def repeat(n, sym): 
  if n <= 0:
    return '' 
  else:
    half = n // 2
    part = repeat(half, sym)
    if n % 2 == 0:
      res = part + part
    else:
      res = part + sym + part
    return res

n = 5
sym = '*'
s = repeat(n, sym)
print()