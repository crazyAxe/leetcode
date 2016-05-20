def getDpArray(arr):
    dp = [0 for x in range(len(arr))]
    dp[0], i = 1, 1
    for i in range(1, len(arr)):
        j = 0
        while j < i:
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j])
            j += 1
        dp[i] += 1
    return dp


def increasingSubqe(arr):
    if len(arr) == 0:
        return 0
    dp = getDpArray(arr)
    res = 0
    for x in dp:
        res = max(res, x)
    return x


arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(increasingSubqe(arr))