from bisect import bisect_left

n = int(input())
(x, y, z) = input().split(maxsplit=3)
(x, y, z) = (int(x), int(y), int(z))
d = list(map(int, input().split(maxsplit=(n - 1))))
cost = [-1] * n
def buy(i: int) -> int:
    if i > n:
        return 0
        
    if cost[i - 1] != -1:
        return cost[i - 1]

    cost[i - 1] = min(
        x + buy(i + 1),
        y + buy(bisect_left(d, d[i - 1] + 7, lo=i, hi=n) + 1),
        z + buy(bisect_left(d, d[i - 1] + 30, lo=i, hi=n) + 1),
    )
    return cost[i - 1]
    
print(buy(1))