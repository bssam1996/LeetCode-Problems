"""
Link: https://leetcode.com/problems/merge-two-sorted-lists
"""


def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    new_list_dict = []
    if list1 is None and list2 is None:
        return None
    while list1 or list2:
        if list1 and list2:
            if list1.val <= list2.val:
                new_list_dict.append(list1)
                list1 = list1.next
            else:
                new_list_dict.append(list2)
                list2 = list2.next
        elif list1:
            new_list_dict.append(list1)
            list1 = list1.next
        elif list2:
            new_list_dict.append(list2)
            list2 = list2.next
    for element in range(len(new_list_dict)):
        if element == len(new_list_dict) - 1:
            new_list_dict[element].next = None
            break
        new_list_dict[element].next = new_list_dict[element + 1]
    return new_list_dict[0]