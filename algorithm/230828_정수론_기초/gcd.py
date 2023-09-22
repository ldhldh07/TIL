def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 예제
print(gcd(56, 48))  # 출력: 8
