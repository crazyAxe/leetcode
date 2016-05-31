# leetcode #25
def reverse_linklist(head, k):
    prev = None
    i = 0
    while head and i < k:
        next = head.next
        head.next = prev
        prev = head
        head = next
        i += 1
    return prev


def reverseKgroup(head, k):
    p = head
    if not head:
        return None
    i = 0
    while i < k and p:
        p = p.next
        i += 1
    if i == k:
        newhead = reverse_linklist(head, k)
        head.next = reverseKgroup(p, k)
        return newhead
    else:
        return head
