from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
s = x*y + y*x
print(s)
#2*x*y
p = x*(x+2*x)
print(p)
#3*x**2
p = (x+2)*(y+3)
print(p)
#(x + 2)*(y + 3)
p = (x+2)*(y+3) + (x+2)*(x-3)
print(p)
#(x - 3)*(x + 2) + (x + 2)*(y + 3)
p = x*(-x+2*x-x)
print(p)
#0
p = (x+2)*(y+3)
print(p.expand())
#x*y + 3*x + 2*y + 6