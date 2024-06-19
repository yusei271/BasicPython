from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import pi

#(1)
a_1 = 0
b_1 = pi / 2 # pi = π
n_1 = 50

h_1 = (b_1 - a_1) / n_1
s = 0

for k in range(1, n_1+1):
    s = s + h_1 / 2 * (sin(a_1 + (k - 1) * h_1) + sin(a_1 + k * h_1))

print("⑴　", s)

#(2)
def f(x):
    return 4 / (1 + x**2)

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))  
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    integral *= h
    return integral

# 区間 [0, 1]
a = 0
b = 1
n = 100  # 任意の分割数

# 積分の実行
result = trapezoidal_rule(f, a, b, n)
print("⑵　", result)

#(3)
import math

def f(x):
    return math.sqrt(math.pi) * math.exp(-x**2)

a = -100
b = 100
n = 1000

dx = (b - a) / n

integral_approx = 0

for i in range(n + 1):
    x_i = a + i * dx
    if i == 0 or i == n:
        # 端点の場合
        integral_approx += f(x_i)
    else:
        # 端点以外の場合
        integral_approx += 2 * f(x_i)

# 最終的な近似値の計算
integral_approx *= dx / 2

print("⑶　", integral_approx)