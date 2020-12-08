def greet():
    global greeting
    greeting = 'Hello ' + name + '!'


name = 'Wim'
greeting = ''
greet()
name = 'Anna'
greet()
name = 'John'
greet()
print()
