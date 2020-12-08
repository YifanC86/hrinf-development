number = 123
print()

numberAsString = str(number)
reverse = ""
palindrome = False

i = len(numberAsString) - 1
while i >= 0:
    reverse = reverse + numberAsString[i]
    i = i - 1
reverse = int(reverse)
if reverse == number:
    palindrome = True

print()
