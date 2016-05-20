def getNext(pattern, next):
    if len(pattern) == 1:
        next[0] = -1
        return next
    next[0] = -1
    next[1] = 0
    pos = 2
    cn = 0 # pos-1 位置的next值，即next[]
    while pos < len(pattern):
        if pattern[pos-1] == pattern[cn]:
            next[pos] = cn + 1
            pos += 1
            cn += 1
        elif cn > 0:
            cn = next[cn]
        else:
            next[pos] = 0
            pos += 1
    return next

def kmp(strs, pattern):
    a = [0 for x in range(len(pattern))]
    next = getNext(pattern, a)
    print(next)
    p = 0 # pattern串指针
    for i in range(len(strs)):
        while p > 0 and strs[i] != pattern[p]:
            p = next[p]
        if pattern[p] == strs[i]:
            p += 1
        if p == len(pattern):
            print("find from %d" % (i- len(pattern) + 1))
            return
    return None
pattern = "bxbababca"
# next = [0 for x in range(len(pattern))]
# getNext(pattern, next)
# print(next)
strs = "ababxbababcadfdsss"
kmp(strs, pattern)

