'''
Link: https://leetcode.com/problems/linked-list-cycle/submissions/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True
            fast = fast.next.next
            slow = slow.next

        return False

    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.val == "cycle":
                return True
            head.val = "cycle"
            head = head.next
        return False