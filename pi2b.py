import decimal
import math
pi = 0.0
decimal.getcontext().prec = 4000
x = 0.0
root = decimal.Decimal(426880*(math.sqrt(10005)))
print(root)
while x < 100000:
    a = (((-1)**decimal.Decimal(x))*(math.factorial(6*decimal.Decimal(x))))/((math.factorial(3*decimal.Decimal(x)))*((math.factorial(decimal.Decimal(x)))**3)*(640320**(3*decimal.Decimal(x))))
    b = decimal.Decimal(x)*decimal.Decimal(a)
    #print(pi)
    #y = x + 0.5
    #pi = pi + 1/(((-1)**x)*(((math.factorial(6*x))/(math.factorial(3*x)))*((math.factorial(x))**3))*((163096908 + (6541681608*x))/(262537412640768000**y)))
    pi = decimal.Decimal(pi) + (decimal.Decimal(pi)-((root)/((math.factorial(6*decimal.Decimal(x)))*((545140134*decimal.Decimal(b))+(135914098*decimal.Decimal(a))))))
    print(pi)
    x=x+1


