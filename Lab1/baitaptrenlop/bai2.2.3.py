from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y 
print(bieuthuc)
#x**2 - x*y + y**2
giatri = bieuthuc.subs({x:3, y:2})
print(giatri)
#7
print(x)
#x
print(y)
#y
giatri = bieuthuc.subs({x:3, y:x})
print(giatri)
#x**2 - 3*x + 9
giatri = bieuthuc.subs({x:y, y:3})
print(giatri)
#9
giatri = bieuthuc.subs({y:x}).subs({x:3})
print(giatri)
#9