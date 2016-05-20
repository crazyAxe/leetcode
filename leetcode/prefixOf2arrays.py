#! /usr/env/bin python3
# -*- coding:utf-8 -*-


def prefixOf2arrays(str1, str2):
    res, i = '', 0
    while i < len(str1) and i < len(str2):
        if str2[i] == str1[i]:
            i += 1
        else:
            break
    res = ''.join(str1[:i])
    return res


def longestCommonPrefix(arrs):
    i, res = 1, arrs[0]
    while i < len(arrs):
        res = prefixOf2arrays(res, arrs[i])
        if len(res) == 0:
            return None
        i += 1
    return res

# --------------------------------binary search method----------------------------------


def isCommonPrefix(arrs, length):
    prefix = arrs[0][0: length+1]
    for strs in arrs:
        if not strs.startswith(prefix):
            return False
    return True


def binaryMatch(arrs):
    minLen = len(arrs[0])
    for strs in arrs:
        if len(strs) < minLen:
            minLen = len(strs)
    low, high = 0, minLen - 1
    while low <= high:
        mid = (low + high) // 2
        if isCommonPrefix(arrs, mid):
            low = mid + 1
        else:
            high = mid - 1
    return arrs[0][0: (high+low)//2+1]


def longestCommonPrefix2(arrs):
    if len(arrs) == 0:
        return ''
    if len(arrs) == 1:
        return arrs[0]
    res = binaryMatch(arrs)
    return ''.join(res)

arrs = ['leets', 'leetcode', 'leetc', 'leetd']
print(longestCommonPrefix2(arrs))