import decimal
import math
decimal.getcontext().prec = 5
n = 0
pi = 0.0
while True:
    a = 2*n+1
    pi, old = ((2**(n+1)*decimal.Decimal(math.factorial(n))**2)/decimal.Decimal(math.factorial(decimal.Decimal(a)))) + decimal.Decimal(pi), pi
    if n % 50 == 0:
       print(pi, n) 
    n += 1
    if pi == old:
        a+=1
        decimal.getcontext().prec = a
        #break
#pi5 ~ 3.141592653589793238462643383|
#                                    wrong-> 27d.p
#pi6 ~ 3.141592653589793|435774089507
#                        wrong-> 15d.p
