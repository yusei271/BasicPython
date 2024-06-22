# (1)
# 自然数を入力
num1 = 61

# 入力された数が素数かどうかを判定する
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    for i in range(2, int(number**0.5 + 1)):
        if number % i == 0:
            return False
    return True

# 素数判定の結果を表示する
if is_prime(num1):
    print(num1, "は素数である")
else:
    print(num1, "は素数でない")

# (2)
# 任意の自然数を入力

num2 = 10

# 入力された数が素数かどうかを判定する
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    for i in range(2, int(number**0.5 + 1 )):
        if number % i == 0:
            return False
    return True

# 素数判定の結果を表示する
if is_prime(num2):
    print(num2, "は素数である")
else:
    print(num2, "は素数でない")

import math

def is_prime(n):
    
    if not isinstance(n, int) or n <= 0:
        return f"{n} は素数でない"

    if n == 1:
        return f"{n} は素数でない"

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return f"{n} は素数でない"

    return f"{n} は素数である"

print(is_prime(3.14))
print(is_prime(-1))