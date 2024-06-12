import decimal
import math
	
def pi1(y, a=5, pi=3.141):
	"""
	Gregory-Leibniz series
	
	gives pi to 'y' decimal places
	pi1(10)
	optional prints
	
	y: decimal places of pi
	a=5: for higher precision (a<y)
	pi=3.141: increaces accuracy
	
	returns: pi	
	"""
	decimal.getcontext().prec = a
	old = 0.0
	x=0.0
	while a < y:
		pi, old, an = decimal.Decimal(pi) + (4*(((-1)**decimal.Decimal(x))/((2*decimal.Decimal(x))+1))), pi, old
		#print(pi/2, a, x)
		x=x+1
		if pi == an:
			#print(pi/2)
			a+=1
			decimal.getcontext().prec = a
	return pi/2
#pi1(10)

def pi2():
	c
#pi2()

def pi3(y, a=5, pi=3.14):
	"""
	infinite series
	
	gives pi to 'y' decimal places
	pi3(10)
	optional prints
	
	y: decimal places of pi
	a=5: for higher precision (a<y)
	pi=3.141: increaces accuracy
	
	returns: pi
	"""
	decimal.getcontext().prec = 5
	a=5
	n = 0.0
	while a<y:
		pi, old = 8*(1/(((4*decimal.Decimal(n))+1)*((4*decimal.Decimal(n))+3))) + decimal.Decimal(pi), pi
		#print(pi, a)
		n += 1
		if pi == old:
			#print(a)
			a = a+1
			decimal.getcontext().prec = a
			
	return pi
#pi3(10)

def pi4(y, a=5):
	"""
	Nilikantha infinite series
	
	gives pi to 'y' decimal places
	pi3(10)
	optional prints
	
	y: decimal places of pi
	a=5: for higher precision (a<y)
	
	returns: pi
	"""
	decimal.getcontext().prec = 5
	n = 2
	pi = 3.0
	while a<y:		
		#print(pi, a)
		pi, old = ((4/(decimal.Decimal(n)*(decimal.Decimal(n)+1)*(decimal.Decimal(n)+2)))-(4/((decimal.Decimal(n)+2)*(decimal.Decimal(n)+3)*(decimal.Decimal(n)+4))))+decimal.Decimal(pi), pi
		n += 4
		if pi == old:
			#print(pi, a)
			a+=1
			decimal.getcontext().prec = a
	return pi
#pi4(10)

def pi5(y, a=5, p=50):
	"""
	infinite series
	
	gives pi to 'y' decimal places
	pi3(10)
	optional prints at every multiple of p
	
	y (int): decimal places of pi
	a=5 (int): for higher precision (a<y)
	p=50 (int): print regulartity
	
	returns: 
	pi: the number pi to y decimal places
	"""
	decimal.getcontext().prec = 5
	n = 0
	pi = 0.0
	while a<y:
		z = 2*n+1
		pi, old = ((2**(n+1)*decimal.Decimal(math.factorial(n))**2)/decimal.Decimal(math.factorial(decimal.Decimal(z)))) + decimal.Decimal(pi), pi
		if n % p == 0:
			pass
		   #print(pi, n) 
		n += 1
		if pi == old:
			print(pi)
			a+=1
			decimal.getcontext().prec = a
	return pi
pi5(10)
