import pickle

with open('c:/Users/wang/Desktop/banner.p', 'rb') as f:
    content = pickle.load(f)
    print(content)

for lists in content:
    for char in lists:
        c, n = char[0], char[1]
        temp = c * int(n)
        print(c, end='')
    print(end='\n')


# 1.学习使用pickle模块进行序列化/反序列化
# 2.每一个tuple指明了字符和该字符的个数
