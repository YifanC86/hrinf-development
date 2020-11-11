bankAccount = 600
cellphoneCost = 300

savingsPerMonth = 350
monthsWaited = 0

while cellphoneCost * 5 > bankAccount:
  bankAccount += savingsPerMonth
  monthsWaited = monthsWaited + 1

bankAccount = bankAccount - cellphoneCost

print()