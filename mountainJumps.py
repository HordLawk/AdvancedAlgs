n = int(input())
h = list(map(int, input().split(maxsplit=(n - 1))))
cost = [-1] * n
for i in range(n, 0, -1):
    if i == n:
        cost[i - 1] = 0
        continue

    step1 = abs(h[i - 1] - h[i])
    if (i + 1) == n:
        cost[i - 1] = step1
        continue

    cost[i - 1] = min(step1 + cost[i], abs(h[i - 1] - h[i + 1]) + cost[i + 1])

print(cost[0])