n = 9385
print()
thousands = n // 1000
hundreds = (n - thousands * 1000)//100
tens = (n - thousands * 1000 - hundreds*100)//10
units = (n - thousands * 1000 - hundreds*100 - tens*10)
print()