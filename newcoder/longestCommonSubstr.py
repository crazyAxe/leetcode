# 左程云 经典算法题精讲（九）-经典动态规划题目大串讲（上）
# still can optimise the space complexity to O(1). review the video to find the solution.
# dp[i][j]: the length of str1 and str2 witch ended must ended with str1[i] and str2[j]. if str1[i] != str2[j]
#            apparently dp[i][j] = 0.


def longest_com_substr(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return None
    maxLen = 0
    index = 0
    dp = [[0 for col in range(len(str2))] for row in range(len(str1))]
    m, n = len(str1), len(str2)

    # init the first row
    for j in range(n):
        if str2[j] == str1[0]:
            dp[0][j] = 1
        else:
            dp[0][j] = 0

    # init the first column
    for i in range(m):
        if str1[i] == str2[0]:
            dp[i][0] = 1
        else:
            dp[i][0] = 0

    # generate the whole dp
    for i in range(1, m):
        for j in range(1, n):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > maxLen:
                    maxLen = dp[i][j]
                    index = i
            else:
                dp[i][j] = 0
    return str1[index-maxLen+1: index+1]

str1 = 'babcd'
str2 = 'cdeabcd'
print(longest_com_substr(str1, str2))