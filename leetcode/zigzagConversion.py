def convert(s, numRows):
    """
        leetcode #6.
        time complexity: O(nm)   or  O(n)? -- only visit each item once.
        space complexity: O(n)
    :param s:
    :param numRows:
    :return:
    """
    if numRows == 1:
        return s
    l = ""
    n = numRows
    d0 = (numRows-1) * 2    # the distance of a round 'V' (from '1' to '7')
    for i in range(numRows):
        j = i
        d = d0 - 2 * i      # the distance of  fore part of a round ( '2' to '6')
        while j < len(s):
            if d > 0:
                l += (s[j])
                j += d
            d = d0 - d      # the distance of  back part of a round ( '6' to '8')
    return l


s = "P"
res = convert(s, 1)
print(res)

#  pictures 
#
# 1      7
# 2    6 8
# 3  5   9
# 4      10