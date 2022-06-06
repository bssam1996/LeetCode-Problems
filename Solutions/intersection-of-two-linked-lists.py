"""
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
"""


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    listA = {}
    while headA:
        listA[headA] = headA
        headA = headA.next
    while headB:
        if listA.get(headB):
            return headB
        headB = headB.next
    return None