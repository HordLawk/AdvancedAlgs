from bisect import bisect_left

(n, m) = input().split()
(n, m) = (int(n), int(m))
playlist = [0]
for i in range(n):
    (c, t) = input().split()
    playlist.append(playlist[i] + (int(t) * int(c)))

moments = input().split(maxsplit=(m - 1))
for moment in moments:
    print(bisect_left(playlist, int(moment), lo=1, hi=n))