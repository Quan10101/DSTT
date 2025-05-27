x = 1
a = x + x + x + 2
print(a)
#5

from sympy import Symbol
x = Symbol('x')
f = x + x + x + 2
print(f)
#3*x + 2

a = Symbol('Noi')
b = Symbol('Chim')
c = 3*b + 7*a
print(c)
#3*Chim + 7*Noi
print(a.name)
print(b.name)
#Noi
#Chim
