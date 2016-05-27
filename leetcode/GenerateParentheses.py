# 22


def help(result, tempStr, leftcount, n):
    # left parentheses > right parentheses
    if leftcount > len(tempStr) - leftcount:
        help(result, tempStr+')', leftcount, n)
    if leftcount < n:
        help(result, tempStr+'(', leftcount+1, n)
    if len(tempStr) == n * 2:
        result.append(tempStr)


def generateParenthesis(n):
    if n == 0:
        return []
    res = []
    help(res, '', 0, n)
    return res


print(generateParenthesis(3))