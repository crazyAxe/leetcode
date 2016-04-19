# 牛课堂算法系列讲座 1.2                        下
# [code = python3.5]                       上    下
# 画出模型可知， 二叉树中序遍历      （低）  上 下 上  下   （顶）


def midOrder(res, n, str):
    if n == 0:
        return None
    midOrder(res, n-1, 'down')
    res.append(str)
    midOrder(res, n-1, 'up')

res = []
midOrder(res, 3, 'down')
print(res)


# class FoldPaper:
#
#     def foldPaperHelper(self, res, n, str):
#         if n==0:
#             return None
#         self.foldPaperHelper(res, n-1, 'down')
#         res.append(str)
#         self.foldPaperHelper(res, n-1, 'up')
#         return res
#
#     def foldPaper(self, n):
#     	res = []
#         self.foldPaperHelper(res, n, 'down')
#         return res