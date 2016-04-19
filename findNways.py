# 有一段楼梯台阶有15级台阶，以小明的脚力一步最多只能跨3级，
# 请问小明登上这段楼梯有多少种不同的走法?()


# def fn1(n):
#     if n <= 0:
#         return None
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#     else:
#         return fn(n-1) + fn(n-2) + fn(n-3)


# https://zh.wikipedia.org/wiki/动态规划     优化算法(空间换时间)
res_dict = {1: 1, 2: 2, 3: 4}
def fn(n):
    if n in res_dict.keys():
        return res_dict[n]
    else:
        res_dict[n] = fn(n-1) + fn(n-2) + fn(n-3)
        return res_dict[n]
res = fn(15)
print(res_dict)
print(res)