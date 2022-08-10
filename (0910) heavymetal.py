with open("0910.txt", "r", encoding="utf-8") as f:
    s = f.readline().replace("heavy", "?").replace("metal", "!")
    ans, qm = 0, 0  # ans - the answer, qm - question marks
    for i in range(len(s)):
        t = s[i]
        if s[i] == "?":
            qm += 1
        elif s[i] == "!":
            ans += qm
    print(ans)
