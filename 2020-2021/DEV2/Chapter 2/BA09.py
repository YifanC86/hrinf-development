def isPrime(n):
  i = 2
  while i <= n/2:
    if n % i == 0:
      return False
    i = i + 1
  return True

def primeSequence(n):
  l = ''
  i = 2
  while i <= n:
    if isPrime(i):
      l = l + str(i) +', '
    i = i + 1
  return l

input = 13
x = isPrime(input)
x = primeSequence(input)
print()
