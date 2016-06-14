#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# leetcode:38


def countAndSay(strs):
    if not strs:
        return None
    res = ''
    count = 0
    temp_char = strs[0]
    for c in strs:
        if c == temp_char:
            count += 1
        else:
            res += str(count)
            res += temp_char
            temp_char = c
            count = 1
    if not res:
        res += str(count)
        res += temp_char
    elif res[-1] != temp_char:
        res += str(count)
        res += temp_char
    return res


def generate(n):
    if not n:
        return None
    res = []
    temp = '1'
    for i in range(n):
        res.append(temp)
        temp = countAndSay(temp)
    return res[-1]

print(generate(4))