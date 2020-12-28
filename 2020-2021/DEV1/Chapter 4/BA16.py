diceone = 1
dicetwo = 2
print()
num = diceone + dicetwo
if num % 2 != 0:
    dishes = 'Mom'
elif num % 4 == 0:
    if diceone == dicetwo:
        dishes = 'Dad'
    else:
        dishes = 'Joe'
else:
    dishes = 'Sue'
print()
