def find_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

# 예제
print(find_divisors(28))  # 출력: [1, 2, 4, 7, 14, 28]
