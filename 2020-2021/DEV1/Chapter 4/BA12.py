paymentMethod = 'Cash on delivery'  # iDeal, Credit Card, Other Payment
deliveryMethod = 'Pickup'  # Home Delivery
billAmount = 700
thresholdAmount = 500
print()
if paymentMethod == 'iDeal':
    pass
elif paymentMethod == 'Cash on delivery':
    billAmount += 5
elif paymentMethod == 'Credit Card' and billAmount < thresholdAmount:
    billAmount += 3
else:
    billAmount += 10
if deliveryMethod == 'Home Delivery' and billAmount < thresholdAmount:
    billAmount += 5
print()
