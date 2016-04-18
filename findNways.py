# 有一段楼梯台阶有15级台阶，以小明的脚力一步最多只能跨3级，
# 请问小明登上这段楼梯有多少种不同的走法?()


def fn(n):
    if n <= 0:
        return None
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return fn(n-1) + fn(n-2) + fn(n-3)

res = fn(15)
print(res)