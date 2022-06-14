"""
Link: https://leetcode.com/problems/merge-nodes-in-between-zeros/
"""


def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr_node = ListNode(val=0, next=None)
    cloned = curr_node
    while head:
        if head.val == 0 and cloned.val != 0 and head.next is not None:
            cloned.next = ListNode(val=0, next=None)
            cloned = cloned.next
        elif head.val != 0:
            cloned.val += head.val
        head = head.next
    return curr_node