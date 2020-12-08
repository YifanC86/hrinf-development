s = ''
start = 1
end = 30
print()

num = start
while num <= end:
    if num % 3 == 0 and num % 5 == 0:
        s = s + "FizzBuzz "
    elif num % 3 == 0:
        s = s + "Fizz "
    elif num % 5 == 0:
        s = s + "Buzz "
    else:
        s = s + str(num) + " "
    num = num + 1

print()
