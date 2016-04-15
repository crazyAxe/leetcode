def findMedianSortedArrays(nums1, nums2):
    from math import ceil
    if len(nums1) == 0:
        return nums2[len(nums2)/2]
    elif len(nums2) == 0:
        return nums1[len(nums1)/2]
    else:

        n = len(nums1) - 1
        m = len(nums2) - 1
        i = j = 0
        res = 0
        while i <= n and j <= m:
            if nums1[i] <= nums2[j]:
                res += 1
                i += 1

                if res == ceil((m+n)/2) + 1:
                    return nums1[i-1]
            else:
                res += 1
                j += 1
                if res == ceil((m+n)/2) + 1:
                    return nums2[j-1]

        if i < n:
            return nums1[(m+n+1)/2 - res + i]
        else:
            return nums2[(m+n+1)//2 - res + j]

res = findMedianSortedArrays([2], [])
print(res)
