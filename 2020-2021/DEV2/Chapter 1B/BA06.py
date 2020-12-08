arg = 123
print()
def reverse(n):
  global rn 
  rn = 0
  while n > 0:
    rn = rn *10 + (n%10) 
    n = n // 10
rn = 0
reverse(arg)
print()