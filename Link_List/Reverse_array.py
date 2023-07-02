#Reverse node in k groups

# Definition for singly-linked list.
from pyrsistent import optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: optional[ListNode],k: int) -> optional[ListNode]:
        cursor = head
        for i in range(k):
            if cursor is None:
                return head
            cursor = cursor.next

        prev = None
        curr = head
        next = None

        count = 0

        while curr is not None and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if next is not None:
            head.next = self.reverseKGroup(next, k)
        
        return prev