# leetcode # 28
# Number（数字）                  包括int,long,float,complex
# String（字符串）                例如：hello,"hello",hello
# List（列表）                    例如：[1,2,3],[1,2,3,[1,2,3],4]
# Dictionary（字典）              例如：{1:"nihao",2:"hello"}
# Tuple（元组）                   例如：(1,2,3,abc)
# Bool（布尔）                    包括True、False


def recurse(dividend, divisor, init_dividor, quotient):
    if divisor < dividend:
        return recurse(dividend, divisor << 1, init_dividor, quotient << 1)
    elif divisor == dividend:
        return quotient
    else:
        if (dividend - (divisor >> 1)) < init_dividor:
            return quotient >> 1
        else:
            return recurse(dividend - (divisor >> 1), init_dividor, init_dividor, 1) + (quotient >> 1)


def divide(dividend, divisor):
    sign = dividend >> 31 + divisor >> 31
    dividend = dividend >> 31 == 0 and dividend or ~dividend+1  # transfer negative to positive
    divisor = divisor >> 31 == 0 and divisor or ~divisor+1
    if divisor > dividend:
        return 0
    quotient = recurse(dividend, divisor, divisor, 1)
    print(quotient)
    quotient = sign == 0 and quotient or ~quotient+1   # add the sign for the quotient
    if -2147483648 <= quotient <= 2147483647:
        return quotient
    else:
        return 2147483647

a = 10
b = 3
print(divide(a, b))