import math

def sin( x, n):
	sine = 0
	for i in range(n):
		sign = (-1)**i
		pi = 22/7
		y = x*(pi/180)
		sine += ((y**(2.0*i+1))/math.factorial(2*i+1))*sign 
	return sine

x = 10

n = 90

print(round(sin(x,n),2))
