"""
Link: https://leetcode.com/problems/symmetric-tree/submissions/
"""


def isSymmetric(self, root) -> bool:
    def checkValueLeft(node):
        if node is None:
            resultleft.append(None)
            return None
        checkValueLeft(node.left)
        checkValueLeft(node.right)
        resultleft.append(node.val)

    def checkValueRight(node):
        if node is None:
            resultright.append(None)
            return None
        checkValueRight(node.right)
        checkValueRight(node.left)
        resultright.append(node.val)

    resultleft = []
    resultright = []
    checkValueLeft(root.left)
    checkValueRight(root.right)
    return resultleft == resultright