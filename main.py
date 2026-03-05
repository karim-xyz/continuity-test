from sympy import symbols, zoo, nan, limit, pretty_print, Reals
from sympy.calculus.util import continuous_domain
from sympy.parsing.sympy_parser import parse_expr

x = symbols("x")

inp = input("f(x) = ")
f = parse_expr(inp, evaluate=False)

c = float(input("c = "))
if c.is_integer():
    c = int(c)

domain = continuous_domain(f, x, Reals)

f_c = f.subs(x, c)
lim_f_x = limit(f, x, c)

pretty_print(f)
print()
print("f(c) = ", f_c)
print()
print("lim f(x) = ", limit(f, x, c, "+"), f"\nx->{c}+")
print()
print("lim f(x) = ", limit(f, x, c, "-"), f"\nx->{c}-")
print()

cond1 = c in domain
cond2 = limit(f, x, c, "+") == limit(f, x, c, "-")
cond3 = f_c == lim_f_x

if cond1 and cond2 and cond3:
    print(f"f is continuous at {c}")
else:
    print(f"f is not continuous at {c}")

