"""
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
"""


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    # Approach but Time Limit Exceeded
    listA = []
    while headA:
        listA.append(headA)
        headA = headA.next
    while headB:
        if headB in listA:
            return headB
        headB = headB.next
    return None