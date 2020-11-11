totalSeconds = 12323
print()
hours = totalSeconds // 3600
minutes = (totalSeconds % 3600) // 60
seconds = totalSeconds % 60

time = str(hours) + ':' + str(minutes) + ':' + str(seconds)

print()