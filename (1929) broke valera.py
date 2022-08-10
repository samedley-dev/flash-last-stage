from bisect import bisect_left

n, k = map(int, input().split())
s = list(map(int, input().split()))
if all(s[i] - s[i - 1] <= k for i in range(1, n)):
    i, scooters = 0, []
    while i < n - 1:
        j = bisect_left(s, s[i] + k)
        if j >= n: j -= 1
        elif s[j] > s[i] + k:
            j -= 1
        former, i = i, j
        scooters.append(s[former])
    print(len(scooters))
else:
    print(-1)
