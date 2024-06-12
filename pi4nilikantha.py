import decimal
import math
decimal.getcontext().prec = 5
n = 2
pi = 3.0
a=5
while True:
    print(pi, a)
    pi, old = (
        (4/(decimal.Decimal(n)*(decimal.Decimal(n)+1)*(decimal.Decimal(n)+2)))
        -(4/((decimal.Decimal(n)+2)*(decimal.Decimal(n)+3)*(decimal.Decimal(n)+4))))+decimal.Decimal(pi), pi
    n += 4
    if pi == old:
        a+=1
        decimal.getcontext().prec = a
        #break
