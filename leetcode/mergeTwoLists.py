class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        p1, p2 = l1, l2
        head = ListNode(0)
        p = head
        while p1 is not None and p2 is not None:
            if p2.val > p1.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p.next.next = None
            p = p.next
        if p1 is not None:
            p.next = p1
        if p2 is not None:
            p.next = p2
        return head.next


def mergeTwoLists2(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1:
        return l2
    if not l2:
        return l1
    start = None
    if l1.val > l2.val:
        start = l2
        start.next = self.mergeTwoLists(l1, l2.next)
    else:
        start = l1
        start.next = self.mergeTwoLists(l1.next, l2)
    return start