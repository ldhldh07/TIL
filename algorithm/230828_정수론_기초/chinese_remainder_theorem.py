# 확장된 유클리드 알고리즘을 이용해 모듈러 역원을 찾는 함수
def mod_inv(a, m):
    g, x, y = extended_gcd(a, m)
    return x % m

# 확장된 유클리드 알고리즘
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# 중국인 나머지 정리 (Chinese Remainder Theorem)
def chinese_remainder_theorem(a, m):
    n = len(a)
    # m의 모든 원소의 곱
    M = 1
    for mi in m:
        M *= mi

    # Mi = M / mi
    M_values = [M // mi for mi in m]

    # 각 Mi에 대한 모듈러 역원 계산: Mi_inv = Mi^-1 mod mi
    M_inv = [mod_inv(M_values[i], m[i]) for i in range(n)]

    # x = a1*M1*M1_inv + a2*M2*M2_inv + ... + an*Mn*Mn_inv (mod M)
    x = sum(a[i] * M_values[i] * M_inv[i] for i in range(n)) % M

    return x

# 예제
a = [2, 3, 1]
m = [3, 5, 7]
print(chinese_remainder_theorem(a, m))  # 출력: 8
