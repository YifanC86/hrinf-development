number = 10
print()
e = 'odd'
p = 'negative'

if number > 0:
    p = 'positive'

if number % 2 == 0:
    e = 'even'

status = f'{number} is {e} and {p}'
print()
