from sympy import Symbol, pprint
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - 2*x*y + y**2
pprint(bieuthuc)
# 2        2
#x -2*x*x+y
from sympy import init_printing, factor
init_printing(oder='rev-lex')
bieuthuc = x*x - 2*x*y + y**2
pprint(bieuthuc)
# 2        2
#x -2*x*x+y
bieuthuc1 = factor(bieuthuc)
pprint(bieuthuc1)
#       2
#(x - y)