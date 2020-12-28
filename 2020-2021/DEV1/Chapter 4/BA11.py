points = 35
totalPoints = 50
print()
percentage = int(points/totalPoints*100)
if percentage < 50:
    remarks = 'Unsatisfactory'
elif percentage >= 50 and percentage < 70:
    remarks = 'Satisfactory'
elif percentage >= 70 and percentage < 90:
    remarks = 'Good'
elif percentage >= 90:
    remarks = 'Excellent'
print()
