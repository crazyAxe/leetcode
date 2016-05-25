def three_sums(array, target):
    if len(array) < 3:
        return []
    i = 0
    nums = sorted(array)
    sum = []
    while i < len(array) - 2:
        left, right = i + 1, len(array) - 1
        while left < right:
            if nums[i] > target:
                break
            temp = nums[i] + nums[left] + nums[right]
            if temp == target:
                sum.append([nums[i], nums[left], nums[right]])
            if temp <= target:
                while nums[left+1] == nums[left] and left + 1 < right:
                    left += 1
                left += 1
            if temp >= target:
                while nums[right-1] == nums[right] and left < right - 1:
                    right -= 1
                right -= 1
        while nums[i] == nums[i+1] and i < len(array) - 2:
            i += 1
        i += 1
    return sum

array = [1, 0, -1, 0, -2, 2]
print(three_sums(array, 3))