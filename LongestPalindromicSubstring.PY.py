# answer1: time exceeded
def printlongestPalindrom(i, n, l):
    if n % 2:
        left = int(i - n/2 + 1)
        right = int(i + n/2)
        return l[left:right+1]
    else:
        left = int(i - n//2)
        right = int(i + n//2)
        return l[left:right+1]

def findlongestPalindrome(s):
    para_len = 0
    para_index = 0
    for i in range(1, len(s)-1):
        offset = 1
        now_len = 0
        # length of substring is even
        while i-offset+1 >= 0 and i+offset < len(s):
            if s[i-offset+1] == s[i+offset]:
                now_len += 2
                offset += 1
                if now_len > para_len:
                    para_index = i
                    para_len = now_len
            else:
                break
        # length of substring is odd
        offset = 1
        now_len = 0
        while i - offset >= 0 and i + offset < len(s):
            if s[i - offset] == s[i + offset]:
                now_len += 2
                offset += 1
                if now_len + 1 > para_len:
                    para_index = i
                    para_len = now_len + 1
            else:
                break

    res = printlongestPalindrom(para_index, para_len, s)
    # for str in res:
    #     print(str, end='')
    print (res.__repr__())

l = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
findlongestPalindrome(l)

# answer by offical
# public String longestPalindrome(String s) {
#     int start = 0, end = 0;
#     for (int i = 0; i < s.length(); i++) {
#         int len1 = expandAroundCenter(s, i, i);
#         int len2 = expandAroundCenter(s, i, i + 1);    <============= THIS IS IMPORTANT HERE !!!!=============
#         int len = Math.max(len1, len2);
#         if (len > end - start) {
#             start = i - (len - 1) / 2;
#             end = i + len / 2;
#         }
#     }
#     return s.substring(start, end + 1);
# }
#
# private int expandAroundCenter(String s, int left, int right) {
#     int L = left, R = right;
#     while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
#         L--;
#         R++;
#     }
#     return R - L - 1;
# }