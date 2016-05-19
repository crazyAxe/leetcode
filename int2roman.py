#! /usr/bin/env python3
# -*- coding:utf-8 -*-


def int2roman(nums):
    '''

    :param nums: given interger( 0 < nums < 4000)
    :return: roman digits
    '''

    trans = {1: 'i', 5: 'v',
             10: 'x', 50: 'l',
             100: 'c', 500: 'd',
             1000: 'm'}
    res, i = '', 1
    while nums:
        mod = nums % 10
        if mod in range(1, 4):
            res = mod * trans[i] + res
        elif mod == 4:
            res = trans[i] + trans[5 * i] + res
        elif mod == 5:
            res = trans[i*5] + res
        elif mod in range(6, 9):
            res = trans[i*5] + (mod - 5) * trans[i] + res
        elif mod == 9:
            res = trans[i] + trans[i*10] + res
        i *= 10
        nums //= 10
    return res

a = 3944
print(int2roman(a))