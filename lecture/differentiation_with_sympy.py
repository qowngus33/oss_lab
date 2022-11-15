import sympy as sp

if __name__ == "__main__":
    x, y = sp.symbols('x y')
    y = 0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4
    yd = sp.diff(y, x)  # Differentiate f with respect to symbols.

    f = sp.sin(sp.cos(x)) * x ** 2
    fd = sp.diff(f)

    fd_at_0 = fd.subs({x: 0})
    print(fd_at_0)
    print(float(yd.subs({x: 2})))

    roots = sp.solveset(y, x)  # Solves a given inequality or equation with set as output
    print(roots)  # FiniteSet(-3.0, 2.0, 9.0)
    r0 = float(roots.args[0])

    sp.pprint(sp.factor(y))  # 인수분해 (factorization)

    y = (x ** 2 - 2 * x + 1)
    sp.pprint(sp.factor(y))

    print(sp.factor(y))
