# leetcode # 27


def remove_element(nums, val):
    if not nums:
        return 0
    start, end = 0, len(nums)-1
    while start < end:
        if nums[start] == val:
            nums[start] = nums[end]
            end -= 1
        else:
            start += 1
    return end + 1

arr = [5, 5]
print(remove_element(arr, 3))