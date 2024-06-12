import decimal

decimal.getcontext().prec = 1
a=1
pi = 0.0
n = 0.0
while True:
    pi, old = 8*(1/(((4*decimal.Decimal(n))+1)*((4*decimal.Decimal(n))+3))) + decimal.Decimal(pi), pi
    print(pi, a)
    n += 1
    if pi == old:
        print(a)
        a = a+1
        decimal.getcontext().prec = a
