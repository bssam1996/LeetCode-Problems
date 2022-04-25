"""
Link: https://leetcode.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        previous_node = ListNode(val=head.val, next=None)
        new_head = None
        head = head.next
        while head:
            nextNode = head.next
            head.next = previous_node
            previous_node = head
            if nextNode is None:
                return head
            head = nextNode
        if head is None:
            return previous_node
        return head