'''
import math
import decimal

decimal.getcontext().prec = 4000
pi = 0.0
x = 0.0
while True:
    #print(pi)
    y = x + 0.5
    pi = decimal.Decimal(pi) + 1/(((-1)**decimal.Decimal(x))*(((math.factorial(6*decimal.Decimal(x)))/(math.factorial(3*decimal.Decimal(x))))*((math.factorial(decimal.Decimal(x)))**3))*((163096908 + (6541681608*decimal.Decimal(x)))/(262537412640768000**decimal.Decimal(y))))
    #pi = (1/(12*((-1)**decimal.Decimal(x))*((decimal.Decimal(math.factorial(6*x))*((545140134*decimal.Decimal(x))+(13591409)))/((math.factorial(3*decimal.Decimal(x)))*(decimal.Decimal(math.factorial(x))**3)*((640320)**((3*decimal.Decimal(x))+(3/2)))))))
    print(pi, x)
    x=x+1

'''
'''
from math import factorial
from decimal import Decimal, getcontext

getcontext().prec=100

def calc(n):
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)
    n = 0
    for k in range(n):
        top = ((-1)**n)*(factorial(6*n))*(13591409+545140134*n)
        bot = factorial(3*n)*(factorial(n)**3)*(640320**((3*n)+1.5))
        pi += Decimal(top)/Decimal(bot)                                   
    pi *= 12
    pi = 1/pi
    return pi
print(calc(25))'''
