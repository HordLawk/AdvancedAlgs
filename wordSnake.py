n,m = [int(x) for x in input().split()]
grid = [list(input()) for _ in range(n)]
k = input()
word = input()
def backtracking(x: int, y: int, i: int) -> bool:
    if (x < 0) or (x > (n - 1)) or (y < 0) or (y > (m - 1)) or (grid[x][y] != word[i]):
        return False
    if i == (len(word) - 1):
        return True
    letter = grid[x][y]
    grid[x][y] = ''
    if(
        backtracking(x - 1, y, i + 1)
        or
        backtracking(x, y + 1, i + 1)
        or
        backtracking(x + 1, y, i + 1)
        or
        backtracking(x, y - 1, i + 1)
    ):
        return True
    grid[x][y] = letter
    return False
found = False
for x in range(n):
    for y in range(m):
        if backtracking(x, y, 0):
            found = True
            break
    if found:
        break
if found:
    print('Yes')
else:
    print('No')
