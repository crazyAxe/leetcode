def binarySearch(arr, len, x):
    '''

    :param arr:
    :param len: arr 数组的最右坐标
    :param x:
    :return:
    '''
    left = 0
    right = len
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return left


def findLIS(arr, dp, length):
    n, res = len(arr) - 1, []
    while dp[n] != length:
        n -= 1
    res.append(arr[n])
    targ = n
    while n >= 0:
        if arr[n] < arr[targ] and dp[n] == dp[targ]-1:
            res.append(arr[n])
            targ = n
        n -= 1
    return (res[::-1])


def lengthOfLIS(arr):
    if len(arr) == 0:
        return 0
    dp, help = [], []  # dp[i]表示以arr[i]结尾的最长递增序列的长度
    help.append(arr[0])
    length = 0 # 表示help数组中当前最后一个值的坐标
    for x in arr:
        pos = binarySearch(help, length, x)
        if pos <= length:
            help[pos] = x
            dp.append(pos+1)   # 根据x (arr[i])在help数组中的位置，更新dp[i], x 在help中是第几个，dp[i]就等几
        else:
            length += 1
            help.append(x)
            dp.append(pos+1)
    print(dp)
    res = findLIS(arr, dp, length+1)
    # return length + 1    # 最长递增子序列的长度
    return res
#########################################################################
#ATTENTION: the sequence dp[:length+1] is not the correct LIS of the array
#           but the same length.
#           For example, if the nums is 1 6 8 5 9
#
#           then the sequence will be like:
#           1
#           1, 6
#           1, 6, 8
#           1, 5, 8
#           1, 5, 8, 9
#
#########################################################################
arr1 = [2, 1, 5, 3, 6, 4, 8, 9, 7]
arr2 = [10, 9, 2, 5, 3, 7, 101, 18]
arr3 = [1, 6, 8, 5, 9]
arr4 = [1, 6, 8, 9 ,2, 3]
print(lengthOfLIS(arr4))
