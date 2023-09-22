def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        print(i)
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [x for x in range(2, limit + 1) if is_prime[x]]

# 소수를 미리 계산한다 (예를 들어, 100까지)
primes = sieve_of_eratosthenes(100)
primes = sieve_of_eratosthenes(20)


# 좀 직관적 코드

def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    primes = []
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return primes

n = 100  # 찾고 싶은 소수들의 범위
print(sieve_of_eratosthenes(n))