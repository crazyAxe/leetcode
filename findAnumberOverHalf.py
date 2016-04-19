# give a list of length N,
# find whether it has a number which exists over N/2 times. return the number or None.
# time complexity : O(n)
# space complexity: O(1)


def findAnumberOverHalf(nums):
    nums2 = nums[:]
    cand = nums2[0]
    times = 1
    i = 1
    while i < len(nums2):
        if times == 0:
            cand = nums[i]
            times = 1
        else:
            if cand == nums2[i]:
                times += 1
            else:
                times -= 1
        i += 1
        # print('candidate: %d, times: %d' % (cand, times))
    return cand


def findResult(nums):
    cand = findAnumberOverHalf(nums)
    count = 0
    for i in nums:
        if i == cand:
            count += 1
    return cand if count >= len(nums)/2 else None

l = [1, 5, 4, 4, 1, 1, 1, 8, 8]
print(findResult(l))