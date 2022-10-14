import sys

sys.setrecursionlimit(10 ** 6)
(h_str, w_str) = input().split(maxsplit=1)
(h, w) = (int(h_str), int(w_str))
grid = []
memo = []
for _ in range(h):
    grid.append(list(input()))
    memo.append([-1] * w)
    
def step(x: int, y: int) -> int:
    if (x > (h - 1)) or (y > (w - 1)) or (grid[x][y] == '#'):
        return 0
    
    if (x == (h - 1)) and (y == (w - 1)):
        return 1

    if memo[x][y] != -1:
        return memo[x][y]
    
    memo[x][y] = (step(x + 1, y) + step(x, y + 1)) % 1000000007
    return memo[x][y]

print(step(0, 0))