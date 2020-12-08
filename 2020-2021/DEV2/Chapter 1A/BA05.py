def even():
    global status
    status = str(n) + ' is Even'


def odd():
    global status
    status = str(n) + ' is Odd'


n = 1
status = ''
if n % 2 == 0:
    even()
else:
    odd()
print()
