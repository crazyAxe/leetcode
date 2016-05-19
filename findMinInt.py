#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# newcoder lesson 6
# given a unsorted integer arrays, find the non-existed minimal positive integer
# [-1, 2, 3, 4 ] return 1
# [4, 1, 2, 3 ] return 5


def findMinInt(arr):
    l = 0
    r = len(arr)
    while l < r:
        if arr[l] == l + 1:
            l += 1
        elif arr[l] <= l or arr[l] > r or arr[arr[l]-1] == arr[l]:
            arr[l] = arr[r-1]
            r -= 1
        else:
            arr[l], arr[arr[l]-1] = arr[arr[l-1]], arr[l]
    return l + 1

a = [1, 2, 3, 5, 7]
print(findMinInt(a))