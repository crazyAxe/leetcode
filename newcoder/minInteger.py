# lesson 6 无序整数数组中没出现的最小正整数
def findMinInt(arr):
    '''

    :param arr:
    :l :当前已收集的最大正整数范围(1 - l)， 同时也是遍历的 left 指针
    :r :在未遍历的数组的最优情况下能收集到的最大整数范围（1 - r）， 同时也是遍历的 right 指针
    :return:数组中未出现的最小正整数
    '''
    l = 0
    r = len(arr)
    while l < r:
        if arr[l] == l + 1:
            l += 1
        elif arr[l] <= l or arr[l] > r or arr[arr[l]-1] == arr[l]:
            arr[l] = arr[r-1] # 因为arr[l]这个数不在收集范围内有价值， 所以将最后一个数arr[r-1] 替换过来
            r -= 1
        else:
            arr[arr[l]-1], arr[l] = arr[l], arr[arr[l]-1]
    return l + 1

arr = [4, 1, 2, 4, 5]
print(findMinInt(arr))