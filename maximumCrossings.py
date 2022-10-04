from heapq import merge
from bisect import bisect_left, bisect_right

def merge_count(arr_a: list[int], size_a: int, arr_b: list[int], size_b: int) -> int:
    crossings = 0
    for e_a in arr_a[bisect_left(arr_a, arr_b[0], hi=size_a):]:
        crossings += bisect_right(arr_b, e_a, hi=size_b)

    return crossings

def sort_count(arr: list[int], size: int) -> tuple[int, list[int]]:
    if size == 1:
        return (0, arr)
    
    half = size // 2
    half2 = size - half
    (r_a, arr_a_sorted) = sort_count(arr[:half], half)
    (r_b, arr_b_sorted) = sort_count(arr[half:], half2)
    r = merge_count(arr_a_sorted, half, arr_b_sorted, half2)
    return (r_a + r_b + r, list(merge(arr_a_sorted, arr_b_sorted)))

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(maxsplit=(n - 1))))
    print(sort_count(arr, n)[0])