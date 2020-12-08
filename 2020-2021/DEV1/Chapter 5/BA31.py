number = 100
print()

wellOrdered = True
if number < 10:
    pass
else:
    numberAsString = str(number)
    num = 1
    while num < len(numberAsString) and wellOrdered:
        if int(numberAsString[num - 1]) >= int(numberAsString[num]):
            wellOrdered = False
        num = num + 1
print()
