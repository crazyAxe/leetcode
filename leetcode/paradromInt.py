# leetcode #9
def paradrom(x, n):
    if n == 1 or n == 0:
        return True
    left = x // pow(10, n-1)
    right = x % 10
    if left == right:
        return paradrom(x%pow(10, n-1)//10, n-2)
    else:
        return False
def paradromInt(num):
    n = 1
    x = num
    while x // 10 != 0:
        n += 1
        x = x // 10
    print(n)
    print(paradrom(num, n))


x = 12147121
paradromInt(x)