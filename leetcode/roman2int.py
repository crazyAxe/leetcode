#! /usr/bin/env python3
# -*- coding:utf-8 -*-


def roman2int(strs):
    trans = {'i': 1, 'v': 5,
             'x': 10, 'l': 50,
             'c': 100, 'd': 500,
             'm': 1000}
    res, i = 0, 0
    while i < len(strs) - 1:    # the last 2 char
        if trans[strs[i]] >= trans[strs[i+1]]:
            res += trans[strs[i]]
        else:
            res -= trans[strs[i]]
        i += 1
    res += trans[strs[i]]
    return res
