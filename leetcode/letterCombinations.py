# 1. Brute force
from functools import reduce


def combination(str1, str2):
    res = []
    for s1 in str1:
        for s2 in str2:
            res.append(s1+s2)
    return res


def transfer_digit(digit):
    return {'1': ' ', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ' '}[digit]


def letter_combination(digits):
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return [x for x in transfer_digit(digits)]
    strs = []
    for digit in digits:
        strs.append(transfer_digit(digit))
    print(strs)
    return reduce(combination, strs)

str1 = 'abc'
str2 = 'def'
str3 = 'ghi'
digits = '2'
print(letter_combination(digits))
# print(reduce(combination, [str1, str2, str3]))
