def reverse(n):
  print()
  rn = 0
  while n>0:
    rn = rn *10 + (n%10) 
    n = n // 10
  return rn
def isPalindrome(n):
  return n == reverse(n)

n = 123
rev = reverse(n)
res = isPalindrome(n)
print()