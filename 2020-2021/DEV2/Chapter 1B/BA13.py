def myrange(init, final, step):
  global seq
  seq = ''
  if step == 0: 
    seq = 'Error: step size cannot be zero'
  else: # is extra and can be omitted
    while (step < 0 and init > final) or (step > 0 and init < final):
      seq = seq + str(init)
      init = init + step

seq = ''
start = 1
end = 10
step = 1
myrange(start, end, step)
print()