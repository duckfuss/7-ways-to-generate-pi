import decimal
x = 1
y = 1
def phi(x, y):
    div = 1
    a=1
    while True:
        decimal.getcontext().prec = a
        x, y = x+y, x
        div, old = decimal.Decimal(x) / decimal.Decimal(y), div
        #print(div)
        if div == old:
            print(div)
            a+= 1

phi(x, y)