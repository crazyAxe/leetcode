#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# find a string's permutation
# （一）递归的全排列算法
#
# （A、B、C、D）的全排列为
#
# 1、A后面跟（B、C、D）的全排列
#
# 2、B后面跟（A、C、D）的全排列
#
# 3、C后面跟（A、B、D）的全排列
#
# 4、D后面跟（A、B、C）的全排列


def swap(arr, p1, p2):
    arr[p1], arr[p2] = arr[p2], arr[p1]
    return arr


def permutation(strs, begin, end):
    '''
    find the permutation of a given string.
    :param strs: the given strings
    :param begin: start index
    :param end: end index
    :return: recursively  print the result
    '''

    if begin == end:
        print(''.join(strs[0:end+1]))
    else:
        for i in range(begin, end+1):
            swap(strs, begin, i)
            permutation(strs, begin+1, end)
            swap(strs, begin, i)

