"""
Link: https://leetcode.com/problems/merge-k-sorted-lists
"""

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        counter = 0
        linked_list = lists[0]
        result = []
        head = linked_list
        while counter < len(lists):
            head = lists[counter]
            while head:
                result.append(head)
                head = head.next
            counter += 1
        if len(result) == 0:
            return None
        result.sort(key=lambda node:node.val)
        for i in range(len(result)-1):
            result[i].next = result[i+1]
        result[-1].next = None
        return result[0]