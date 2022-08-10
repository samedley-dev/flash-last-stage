def is_sorted_fw(N, K):
    s = str(K)
    for i in range(1, N):
        if s[i - 1] >= s[i]:
            return False
    return True


def is_sorted_bw(N, K):
    s = str(K)
    for i in range(1, N):
        if s[i - 1] <= s[i]:
            return False
    return True


def is_magical(N, K):
    return is_sorted_fw(N, K) or is_sorted_bw(N, K)


if is_magical(int(input()), int(input())):
    print("y")
else:
    print("n")
