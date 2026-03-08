from sympy import symbols, zoo, nan, limit, pretty_print, Reals
from sympy.calculus.util import continuous_domain
from sympy.parsing.sympy_parser import parse_expr
from graph import draw

x = symbols("x")

inp = input("f(x) = ")
f = parse_expr(inp, evaluate=False)

c = float(input("c = "))
if c.is_integer():
    c = int(c)

domain = continuous_domain(f, x, Reals)

f_c = f.subs(x, c)
lim_f_x = limit(f, x, c)

#f(c) exists
cond1 = c in domain
#f has a limit as x->c
cond2 = limit(f, x, c, "+") == limit(f, x, c, "-")
#the limit equals the function value
cond3 = f_c == lim_f_x

if cond1 and cond2 and cond3:
    print(f"f is continuous at {c}")
else:
    print(f"f is not continuous at {c}")

disp = input("display a graph? [y/N] ")
if disp == "y":
    draw(f, x)

