from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import pi

a = 0
b = pi / 2 # pi = π
n = 100

h = (b - a) / n
s = 0

for k in range(0, n+1):
    s = s + h / 2 * (sin(a + (k - 1) * h) + sin(a + k * h))

print("求める積分値:", s)