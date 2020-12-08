def greeting(name, gender):
    global s
    s = 'Hello, '
    if gender == 'M':
        s = s + 'mister '
    elif gender == 'F':
        s = s + 'miss '
    s = s + name + '.'


s = ''
name = 'n'
gender = 'g'
greeting(name, gender)
print()
