def findMedianSortedArrays(nums1, nums2):
    nums3 = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1
        else:
            nums3.append(nums2[j])
            j += 1
    while j < len(nums2):
        nums3.append(nums2[j])
        j += 1
    while i < len(nums1):
        nums3.append(nums1[i])
        i += 1
    if len(nums3) % 2:
        return nums3[len(nums3)//2]
    else:
        # there must be a ' * 1.0 ' to transfer to float result, or you will get wrong!!
        return (nums3[int(len(nums3)/2)] + nums3[int(len(nums3)/2 - 1)]) * 1.0 / 2

