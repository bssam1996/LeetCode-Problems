"""
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


def maxDepth(self, root: Optional[TreeNode]) -> int:
    def checkValue(node, level):
        if node is None:
            return level
        a = checkValue(node.left, level + 1)
        b = checkValue(node.right, level + 1)
        return a if a > b else b

    return checkValue(root, 0)