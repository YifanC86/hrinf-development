n = 27
print()
isPrime = True
if n <= 1 or n % 1 > 0:
    isPrime = False
for i in range(2, n // 2):
    if n % i == 0:
        isPrime = False

print()
