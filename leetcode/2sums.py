def quickSort(arr, left, right):
    if len(arr) == 0:
        return None
    if left < right:
        low, high = left, right
        temp = arr[low]
        while low < high:
            while low < high and arr[high] > temp:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] <= temp:
                low += 1
            arr[high] = arr[low]
            arr[low] = temp
        quickSort(arr, left, low-1)
        quickSort(arr, low+1, right)


def binarySearch(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return None

# arr = [1, 8, 3, 4, 2, 6]
# print(binarySearch(arr, 0))


def twoSums(nums, value):
    arr = nums[:]
    quickSort(arr, 0, len(arr)-1)
    print(arr)
    res, n = [], 0
    for i in range(len(arr)-1):
        j = binarySearch(arr[i+1:], value-arr[i])
        if j is not None:
            res.append([])
            res[n].append(arr[i])
            res[n].append(arr[i+1:][j])
            n += 1
    return res


arr = [-1, -1, 0, 1, 2, 4]
# print(binarySearch(arr, 4))
print(twoSums(arr, 3))