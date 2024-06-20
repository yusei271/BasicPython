from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import pi

import math

def trapezoidal_integration(f, a, b, n):
    
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    integral *= h
    return integral

# (1) 
def f1(x):
    return math.sin(x)

a1, b1, n1 = 0, math.pi / 2, 50
integral1 = trapezoidal_integration(f1, a1, b1, n1)
print(f"⑴: {integral1}")

# (2) 
def f2(x):
    return 4 / (1 + x**2)

a2, b2, n2 = 0, 1, 100
integral2 = trapezoidal_integration(f2, a2, b2, n2)
print(f"⑵: {integral2}")

# (3) 
def f3(x):
    return math.sqrt(math.pi) * math.exp(-x**2)

a3, b3, n3 = -100, 100, 1000
integral3 = trapezoidal_integration(f3, a3, b3, n3)
print(f"⑶: {integral3}")