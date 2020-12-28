day = 20
month = 12
print()
if month in (1, 2, 3):
    season = 'Winter'
elif month in (4, 5, 6):
    season = 'Spring'
elif month in (7, 8, 9):
    season = 'Summer'
else:
    season = 'Autumn'

if (month == 3) and (day > 20):
    season = 'Spring'
elif (month == 6) and (day > 20):
    season = 'Summer'
elif (month == 9) and (day > 21):
    season = 'Autumn'
elif (month == 12) and (day > 20):
    season = 'Winter'
print()
