import decimal
import math
n = 1.0
pi = 1
decimal.getcontext().prec = 1000
while True:
    num = 4*(decimal.Decimal(n**2))
    pi, old = (decimal.Decimal((num)/(num-1))) * decimal.Decimal(pi), pi
    print(2*pi, n)
    #print(2*n, 2*n-1)
    n+=1
    if pi == old:
        print(2*pi, n)
        break
    
