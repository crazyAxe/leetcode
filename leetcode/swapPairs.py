# leetcode #24
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# accepted
def swap_pairs(head):
    if not head:
        return None
    if not head.next:
        return head
    t, front, behind = ListNode(0), head.next, head
    front = head
    while front:
        if front.next:
            behind.next = front.next
            front.next = behind
            t.next = front
            t = behind
            behind = behind.next
            front = behind.next
        else:
            t.next = front
            front.next = behind
            behind.next = None
            front = behind.next

    return head


# accepted
def swap_pairs2(head):
    if head and head.next:
        temp = head.next
        temp.next = swap_pairs(temp.next)
        temp.next = head
        return temp
    else:
        return head

