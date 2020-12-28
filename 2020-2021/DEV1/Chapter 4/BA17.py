n = 123
print()

temp = n
rev = 0
while(temp > 0):
    dig = temp % 10
    rev = rev * 10 + dig
    temp = temp // 10
if n == rev:
    output = str(n) + ' is a palindrome'
else:
    output = str(n) + ' is NOT a palindrome'

print()
