def second_pick(arrs, i, j):
    if i == j:
        return 0
    return min(first_pick(arrs, i+1, j), first_pick(arrs, i, j-1))


def first_pick(arrs, i, j):
    if i == j:
        return arrs[i]
    return max(arrs[i]+second_pick(arrs, i+1, j), arrs[j]+second_pick(arrs, i, j-1))


def win(arrs):
    if not arrs or len(arrs) == 0:
        return None
    return max(first_pick(arrs, 0, len(arrs)-1), second_pick(arrs, 0, len(arrs)-1))


# dynamic programing
# f[end][start] means max point when first_pick in sequence(start, end)
def win2(arrs):
    s = [[0 for start in range(len(arrs)) if end >= start] for end in range(len(arrs))]
    f = [[0 for start in range(len(arrs)) if end >= start] for end in range(len(arrs))]
    for end in range(len(arrs)):
        f[end][end] = arrs[end]
        for start in range(end-1, -1, -1):  # start in (end-1, end-2, ..., 0)
            f[end][start] = max(arrs[start] + s[end][start+1], arrs[end] + s[end-1][start])
            s[end][start] = min(f[end][start+1], f[end-1][start])
    return max(f[len(arrs)-1][0], s[len(arrs)-1][0])


arrs = [1, 4, 2, 5, 3]
print(win2(arrs))