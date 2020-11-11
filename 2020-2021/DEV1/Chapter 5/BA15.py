isItDay = False
isItNight = not isItDay

hour = 0
while hour < 24:
  if hour >= 6 and hour <= 17:
    isItDay = True
  else:
    isItDay = False
  isItNight = not isItDay
  hour = hour + 1

print()