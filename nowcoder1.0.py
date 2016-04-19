# circle print a square.
# @para:start   mark the up left index,
# @para:end    mark the low right index,


def circlePrint(l, start, end):
    if start == end:
        print(l[start][end])

    else:
        i = j = start
        while i <= end:
            print(l[i][j])
            i += 1
        i -= 1
        j += 1

        while j <= end:
            print(l[i][j])
            j += 1
        j -= 1
        i -= 1

        while i >= start:
            print(l[i][j])
            i -= 1
        i += 1
        j -= 1

        while j >= start:
            print(l[i][j])
            j -= 1
        j += 1
        circlePrint(l, start+1, end-1)
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
circlePrint(l, 0, 2)