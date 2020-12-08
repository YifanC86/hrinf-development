def greet():
    global greeting
    if age != 1:
        greeting = 'Hello ' + name + '! You are ' + str(age) + ' years old.'
    else:
        greeting = 'Hello ' + name + '! You are ' + str(age) + ' year old.'


name = 'Wim'
age = 32
greeting = ''
greet()
name = 'Anna'
age = 1
greet()
name = 'John'
age = 0
greet()

print()
