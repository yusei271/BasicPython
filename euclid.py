# TODO

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#問⑴
num1_1 = 10
num1_2 = 20

result_1 = gcd(num1_1, num1_2)

print("⑴の最大公約数:", result_1)

#問⑵
num2_1 = 14
num2_2 = 91

result_2 = gcd(num2_1, num2_2)

print("⑵の最大公約数:", result_2)

#問⑶
num3_1 = 91
num3_2 = 14

result_3 = gcd(num3_1, num3_2)

print("⑶の最大公約数:", result_3)

