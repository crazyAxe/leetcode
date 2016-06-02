# reverse the stack elements and can't apply space on your own
def remove_last_stack_element(stack):
    res = stack.pop()
    if not stack:
        return res
    else:
        last = remove_last_stack_element(stack)
        stack.append(res)
        return last


def reverse_stack(stack):
    if not stack:
        return
    res = remove_last_stack_element(stack)
    reverse_stack(stack)
    stack.append(res)



stack = [3, 2, 1]
reverse_stack(stack)
print(stack)
