N = int(input())
solutions = list(map(int, input().split()))

start, end = 0, N-1
min_value = float('inf')

answer = (0, 0)
while start < end:
    mix = solutions[start] + solutions[end]
    
    if abs(mix) < min_value:
        min_value = abs(mix)
        answer = (solutions[start], solutions[end])

    if mix < 0:
        start += 1
    else:
        end -= 1

print(*answer)
