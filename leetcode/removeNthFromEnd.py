class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return
        quick, slow = head, head
        for i in range(n):
            quick = quick.next

        # if the quick is None, it means remove the Nth listNode from the end of N-length list. so just remove
        # the first node
        if quick is None:
            head = head.next
            return head

        while quick.next is not None:
            slow = slow.next
            quick = quick.next
        slow.next = slow.next.next
        return head

head = ListNode(2)
l1 = ListNode(3)
head.next = l1
p = head
# while p is not None:
#     print(p.val)
#     p = p.next
s = Solution()
s.removeNthFromEnd(head, 2)