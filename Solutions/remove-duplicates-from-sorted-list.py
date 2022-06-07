"""
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list
"""


def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    original_head = head
    curr = head
    head = head.next
    while head:
        if head.val == curr.val:
            curr.next = head.next
        else:
            curr = head
        head = head.next
    return original_head
