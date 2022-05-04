"""
Link: https://leetcode.com/problems/palindrome-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        array = []
        while current != None:
            array.append(current.val)
            current = current.next
        return self.is_array_palingdrom(array)

    def is_array_palingdrom(self, array):
        if len(array) == 1:
            return True
        if len(array) % 2 == 1:
            del array[int(len(array) / 2)]
        first_half = array[0:int(len(array) / 2)]
        second_half = array[-1:int(len(array) / 2) - 1:-1]
        return first_half == second_half
