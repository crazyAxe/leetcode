def is_valid(strs):
    stack = [strs[0]]
    i = 1
    matches = {'(': ')', '[': ']', '{': '}'}
    while i < len(strs):
        if strs[i] in matches.keys():
            stack.append(strs[i])
            if len(stack) > 1 and stack[-1] > stack[-2]:
                return False
        else:
            s = stack.pop()
            if matches.get(s) != strs[i]:
                return False
        i += 1
    return True

strs = '([])'
print(is_valid(strs))