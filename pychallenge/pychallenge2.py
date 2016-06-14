# solution1
file_object = open('c:/Users/wang/Desktop/orc.txt')
text = file_object.read()
res = ''
for ch in text:
    if 'a' <= ch <= 'z':
        res += ch
file_object.close()
print(res)


# # solution2
# import collections
# file_object = open('C:/Users/wang/Desktop/orc.txt')
# try:
#     all_text = file_object.read()
# finally:
#     file_object.close()
#
#
# char_dict = collections.OrderedDict()
# for c in all_text:
#     char_dict[c] = char_dict.get(c, 0) + 1
# ave_fre = len(all_text) // len(char_dict)
# result = ''
# for (key, value) in char_dict.items():
#     if value < ave_fre:
#         result += key
#
# print(char_dict)
# print(ave_fre)
# print(result)
