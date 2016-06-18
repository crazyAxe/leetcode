import re, zipfile


base_dir = 'c:/Users/wang/Desktop/channel/'
text = '90052'
data = re.search(r"[0-9]+$", text)
zip_file = zipfile.ZipFile('c:/Users/wang/Desktop/channel.zip', 'r')
comment = []
print(data)
while data:
    spec_dir = str(data.group()) + '.txt'
    dir = base_dir + spec_dir
    comment.append(zip_file.getinfo(spec_dir).comment.decode())
    with open(dir, 'r') as f:
        text = f.read()
        data = re.search(r"[0-9]+$", text)
print(''.join(comment))


# 学习使用zipfile模块，从ZipFile中获取comment信息