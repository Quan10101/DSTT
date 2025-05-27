from sympy import Symbol, solve
x = Symbol('x')
bieuthuc = x + 3 - 5
print(solve(bieuthuc))
#2
bieuthuc = x**2 + 3 - 5 
nghiemx = solve(bieuthuc) 
print(nghiemx)
#[-sqrt(2), sqrt(2)]
print(nghiemx[0])
#-sqrt(2)
print(nghiemx[1])
#sqrt(2)