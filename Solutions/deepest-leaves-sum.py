"""
Link: https://leetcode.com/problems/deepest-leaves-sum/
"""


def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    def scanTree(node, level):
        if node is None:
            return None
        if len(result) > level:
            result[level] += node.val
        else:
            result.append(node.val)
        scanTree(node.right, level + 1)
        scanTree(node.left, level + 1)

    result = []
    scanTree(root, 0)
    return result[-1]