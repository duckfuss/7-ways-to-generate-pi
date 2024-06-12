import decimal
import math
n = 1
decimal.getcontext().prec = 1000
pi = 1.0
a=1000
old = math.sqrt(2)
while True:
    pi, prev = decimal.Decimal((decimal.Decimal(old)/2) * decimal.Decimal(pi)), pi
    if n % 500 == 0:
       print(2/pi, n)
    old = decimal.Decimal(math.sqrt(2 + decimal.Decimal(old)))
    n+=1
    if pi == prev:
        a+=1
        decimal.getcontext().prec = a
        #break
#pi5 ~ 3.141592653589793238462643383|
#                                    wrong-> 27d.p
#pi6 ~ 3.141592653589793|435774089507
#                        wrong-> 15d.p
