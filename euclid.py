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

def are_coprime(a, b):
    return gcd(a, b) == 1

def print_coprime_status(a, b):
    if are_coprime(a, b):
        print("互いに素である")
    else:
        print("互いに素でない")

print_coprime_status(8, 15)

# エクストラ問題

import random

def random_coprime_pairs_count(num_pairs):
    count_coprime = 0
    
    for _ in range(num_pairs):
        a = random.randint(1, 10000)
        b = random.randint(1, 10000)
        
        if are_coprime(a, b):
            count_coprime += 1
    
    return count_coprime

num_pairs = 100000
count_coprime = random_coprime_pairs_count(num_pairs)
probability_coprime = count_coprime / num_pairs

print(f"確率：{probability_coprime:.10f}")