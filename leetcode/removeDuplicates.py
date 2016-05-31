# leetcode #26
def removeDuplicates(arrs):
    if not arrs:
        return 0
    j = 1
    for i in range(1, len(arrs)):
        if arrs[i] != arrs[i - 1]:
            arrs[j] = arrs[i]
            j += 1
    return j


arr = [1, 1]
removeDuplicates(arr)