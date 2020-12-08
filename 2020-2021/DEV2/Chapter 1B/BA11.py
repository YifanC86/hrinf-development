def ones(p):
    global s
    if p == 1:
        s = s + 'one'
    elif p == 2:
        s = s + 'two'
    elif p == 3:
        s = s + 'three'
    elif p == 4:
        s = s + 'four'
    elif p == 5:
        s = s + 'five'
    elif p == 6:
        s = s + 'six'
    elif p == 7:
        s = s + 'seven'
    elif p == 8:
        s = s + 'eight'
    elif p == 9:
        s = s + 'nine'
    
def tens(p):
    global s
    if p == 2:
        s =  'twenty'
    elif p == 3:
        s = 'thirty'
    elif p == 4:
        s = 'forty'
    elif p == 5:
        s = 'fifty'
    elif p == 6:
        s =  'sixty'
    elif p == 7:
        s =  'seventy'
    elif p == 8:
        s = 'eighty'
    elif p == 9:
        s =  'ninety'

def inwords(p):
  global s
  if p >= 20 and p < 100:
    if p // 10 > 1: 
      tens(p//10)
    if p % 10 > 0: 
      s = s + ' '
      ones(p%10)

step = 7
i = 20 
while i < 100:
    s = ''
    inwords(i)
    i = i + step