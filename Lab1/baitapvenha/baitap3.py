from sympy import Symbol, solve
x = Symbol('x') 
a = Symbol('a') 
b = Symbol('b') 
c = Symbol('c')
ptb2 = a*x*x + b*x + c
nghiem = solve(ptb2, x, dict = True)
print(nghiem)\
#[{x: (-b - sqrt(-4*a*c + b**2))/(2*a)}, {x: (-b + sqrt(-4*a*c + b**2))/(2*a)}]
