# leetcode #23
# Definition for singly-linked list.

import math

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge2list(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    head = ListNode(0)
    p = head
    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    if l1:
        p.next = l1
    if l2:
        p.next = l2
    return head.next


def mergeKlist(lists):
    n = len(lists)
    if n == 0:
        return None
    if n == 1:
        return lists[0]
    while n > 1:
        temp = []
        for i in range(0, n, 2):
            if i+1 < n:
                temp.append(merge2list(lists[i], lists[i+1]))
            else:
                temp.append(lists[i])
        lists = temp
        n = len(lists)
    return lists[0]

l1 = ListNode(2)
l2 = []
l3 = ListNode(-1)
mergeKlist([l1, l2, l3])