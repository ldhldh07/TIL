def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 예시
print(gcd(56, 98))  # 14
print(gcd(98, 56))  # 14
