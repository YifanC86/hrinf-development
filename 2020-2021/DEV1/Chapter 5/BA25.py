start = 100
end = 999
print()

res = ''
num = start
while num <= end:
    temp = num
    rev = 0
    while(temp > 0):
        dig = temp % 10
        rev = rev * 10 + dig
        temp = temp // 10
    if num == rev:
        res = f"{res}{num}\n"
    num = num + 1

print()
