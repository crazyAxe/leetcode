import re
file_object = open('C:/Users/wang/Desktop/re.txt')
text = file_object.read()
pattern = re.compile(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
res = re.findall(pattern=pattern, string=text)
file_object.close()
print(''.join(res))

# 注意re.match(), re.search(), 与re.findall()的区别