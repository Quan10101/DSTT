from sympy import Symbol, factor
x = Symbol('x')
y = Symbol('y')
bieuthuc = x**3 - y**3
print(factor(bieuthuc))
#(x - y)*(x**2 + x*y + y**2)

from sympy import expand
bieuthuc = (x - y)*(x**2 + x*y + y**2) 
print(expand(bieuthuc))
#x**3 - y**3