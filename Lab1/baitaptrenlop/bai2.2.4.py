from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
print(bieuthuc)
#x**2 - x*y + y**2 
bieuthuc_moi = bieuthuc.subs({x:1-y})
print(bieuthuc_moi)
#y**2 - y*(1 - y) + (1 - y)**2
from sympy import simplify
dongian = simplify(bieuthuc_moi)
print(dongian)
#3*y**2 - 3*y + 1
from sympy import Symbol 
from sympy import sin, cos 
x = Symbol('x') 
y = Symbol('y') 
bt = sin(x)*cos(y) + cos(x)*sin(y) 
bt_moi = simplify(bt) 
print(bt_moi)
#sin(x + y)