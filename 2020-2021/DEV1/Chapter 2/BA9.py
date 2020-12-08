wWidth = 8
wHeight = 3
wThickness = 2
costPerCubicMeter = 250
dWidth = 1
dHeight = 2
doorPrice = 500

wArea = wWidth * wHeight
dArea = dWidth * dHeight
concreteRequired = (wArea - dArea) * wThickness
totalCost = concreteRequired * costPerCubicMeter + doorPrice
print()
