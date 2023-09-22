def prime_factors(n):
    factors = []
    # 2로 나눌 수 있는 경우 모두 나눈다.
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # 이제 n은 홀수이다. 3부터 sqrt(n)까지의 모든 숫자로 나누어본다.
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    
    # 남은 n이 2보다 크면 이것은 소수이다.
    if n > 2:
        factors.append(n)
    
    return factors

# 예제
print(prime_factors(315))  # 출력: [3, 3, 5, 7]
