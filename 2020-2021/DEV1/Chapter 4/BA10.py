year = 2019
print()
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            isLeap = True
        else:
            isLeap = False
    else:
        isLeap = True
else:
    isLeap = False
print()
