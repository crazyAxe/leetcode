def ExpandAroundCenter(arr, center, r):
    i = center - r
    j = center + r
    while i>=0 and j<len(arr) and arr[i]==arr[j]:
        i -= 1
        j += 1
    return j - center


def preArray(arr):
    return "#" + "#".join(arr) + "#"


def postArray(arr):
    res = ''
    for i in arr:
        if i != "#":
            res += i
    return res


def getResult(arr, parr):
    max = parr[0]
    index = 0
    for i in range(len(parr)):
        if parr[i] > max:
            max = parr[i]
            index = i
    left = index - parr[index] + 1
    right = index + parr[index] - 1
    return arr[left:right+1]


def getLongestPalindrome(strs):
    arr = preArray(strs)
    parr = [0 for i in range(len(arr))]

    # 初始化
    index = 0
    pright = 1

    for i in range(len(arr)):
        j = index * 2 - i   # j is a symmertrical point of i against index
        if i < pright:
            if (j - parr[j]) > (index - parr[index]):
                parr[i] = parr[j]
            elif (j - parr[j]) < (index - parr[index]):
                parr[i] = pright - i
            else:
                parr[i] = ExpandAroundCenter(arr, i, parr[j])
                pright = i + parr[i]
                index = i
        else:
            parr[i] = ExpandAroundCenter(arr, i ,0)
            pright = i + parr[i]
            index = i
    print(parr)

    res = getResult(arr, parr)
    print(postArray(res))
    return postArray(res)

l1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
getLongestPalindrome(l1)