def table(n,m):
  global final
  final  = ''
  i = 1
  while i <= m:
    row = str(n) + ' x ' +str(i) +' = ' +str(i*n)
    final = final + row + '\n'
    i = i + 1

final = ''
table(4, 5)
table(3, 10)
print() 