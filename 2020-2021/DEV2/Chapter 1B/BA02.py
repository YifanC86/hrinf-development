def difference(a, b):
    global res
    res = a - b
    if res < 0:
        res = res * -1


res = 0
difference(9, 3)
difference(3, 9)
difference(res, res)
print()
