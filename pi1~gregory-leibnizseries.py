import decimal

decimal.getcontext().prec = 5
pi = 3.141
x = 0.0
old = 0.0
a = 5
while True:
    pi, old, an = decimal.Decimal(pi) + (4*(((-1)**decimal.Decimal(x))/((2*decimal.Decimal(x))+1))), pi, old
    print(pi/2, a, x)
    x=x+1
    if pi == an:
        a+=1
        decimal.getcontext().prec = a
        #break
