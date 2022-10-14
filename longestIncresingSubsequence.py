n = int(input())
a = list(map(int, input().split(maxsplit=(n - 1))))
lis = [-1] * n
def calcLIS(i: int) -> int:
    if lis[i] != -1:
        return lis[i]
    
    lis[i] = 1 + max([calcLIS(j) for j,e in enumerate(a) if (e > a[i]) and (j > i)] + [0])
    return lis[i]

print(max([calcLIS(i) for i in range(n)]))