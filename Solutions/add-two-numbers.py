"""
Link: https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        first_number = ""
        while head:
            first_number = str(head.val) + first_number
            head = head.next
        head = l2
        second_number = ""
        while head:
            second_number = str(head.val) + second_number
            head = head.next
        result = str(int(first_number) + int(second_number))
        head = ListNode(val=result[-1],next=None)
        total_count = len(result)
        if total_count == 1:
            return head
        else:
            tail = ListNode(val=result[-2],next=None)
            head.next = tail
        for character in range(len(result)-3, -1, -1):
            current_node = ListNode(val=result[character], next=None)
            tail.next = current_node
            tail = tail.next
        return head
