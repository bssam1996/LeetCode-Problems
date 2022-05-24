"""
Link: https://leetcode.com/problems/same-tree/
"""


def isSameTree(self, p, q):
    def checkValue1(node):
        if node is None:
            result1.append(None)
            return None
        result1.append(node.val)
        checkValue1(node.left)
        checkValue1(node.right)

    def checkValue2(node):
        if node is None:
            result2.append(None)
            return None
        result2.append(node.val)
        checkValue2(node.left)
        checkValue2(node.right)

    result1 = []
    result2 = []
    checkValue1(p)
    checkValue2(q)
    return result1 == result2

