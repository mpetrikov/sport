def lcs_len(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    f = [[0] * (l2 + 1) for i in range(l1+1)]
    for i in range(1, l1+1):
        for j in range(1, l2 + 1):
            if s1[i-1] == s2[j-1]:
                f[i][j] = f[i-1][j-1] + 1
            else:
                f[i][j] = max(f[i - 1][j], f[i][j-1])
    return f[l1][l2]
