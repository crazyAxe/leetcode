# 左程云 经典算法题精讲（九）-经典动态规划题目大串讲（上）
# still can optimise the space complexity
# dp[i][j] : length of str1[:i+1] and str2[:j+1] 's common sub-sequence


def generateDp(str1, str2):
    m, n = len(str1), len(str2)
    i, j = 0, 0
    arr = [[0 for col in range(len(str2))] for row in range(len(str1))]
    # init the first row
    while j < n:
        if str2[j] != str1[0]:
            arr[0][j] = 0
            j += 1
        else:
            for k in range(j, n):
                arr[0][k] = 1
            break

    # init the first column
    while i < m:
        if str1[i] != str2[0]:
            arr[i][0] = 0
            i += 1
        else:
            for k in range(i, m):
                arr[k][0] = 1
            break

    # generate whole dp array
    for i in range(1, m):
        for j in range(1, n):
            if str1[i] == str2[j]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
    return arr


def long_commom_subseq(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return []
    res = []
    dp = generateDp(str1, str2)
    i, j = len(str1) - 1, len(str2) - 1
    while i > 0 and j > 0:
        if dp[i][j] > dp[i-1][j] and dp[i][j] > dp[i][j-1]:
            res.append(str1[i])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1
    # verify the last border value
    if dp[i][j] == 1:
        res.append(str1[0])
    return ''.join(res[::-1])
str1 = ''
str2 = 'babcd'
print(long_commom_subseq(str1, str2))

