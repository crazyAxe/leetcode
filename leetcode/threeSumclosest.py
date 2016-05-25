def threeSumcloest(arrs, target):
    if len(arrs) < 3:
        return sum[arrs]
    nums = sorted(arrs)
    i = 0
    sums, temp, diff = 0, 0, 65536
    while i < len(nums) - 2:
        left, right = i + 1, len(nums) - 1
        while left < right:
            temp = nums[i] + nums[left] + nums[right]
            if abs(temp - target) < diff:
                diff = abs(temp - target)
                sums = temp
            if temp == target:
                return sums
            if temp < target:
                left += 1
            if temp > target:
                right -= 1
        i += 1
    return sums


arrs = [0,2,1,-3]
print(threeSumcloest(arrs, 1))