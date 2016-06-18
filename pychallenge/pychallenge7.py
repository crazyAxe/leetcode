# refer to blog: http://blog.csdn.net/BillStone/article/details/4489329
# the most import is that you should consider the picture as a digit data. thus transfer it to the byte format.

from PIL import Image
image = Image.open('/home/wang/Downloads/oxygen.png')
data = image.convert('L').getdata()
print(data.size)
res = ''
for i in range(3, 608, 7):
    res += chr(data[image.size[0]*50+i])
print(res)