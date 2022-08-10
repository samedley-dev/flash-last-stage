def is_palindrome(s):
    s = str(s)
    return s == s[::-1]


lychrels = 0
for i in range(1, 10000):
    N, its, flag = i, 0, False
    while its < 50 and not flag:
        N = N + int(str(N)[::-1])
        if is_palindrome(N):
            flag = True
        else:
            its += 1
    if not flag:
        lychrels += 1
print(lychrels)  # 249
 
