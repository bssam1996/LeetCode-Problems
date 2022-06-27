"""
Link: https://leetcode.com/problems/reorder-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        linked_list = []

        while head:
            next_head = head.next
            linked_list.append(head)
            head.next = None
            head = next_head
        head = linked_list[0]
        right = True
        counter_right = len(linked_list) - 1
        counter_left = 1
        for element in range(len(linked_list) - 1):
            if right:
                head.next = linked_list[counter_right]
                head = head.next
                right = False
                counter_right -= 1
            else:
                head.next = linked_list[counter_left]
                head = head.next
                right = True
                counter_left += 1