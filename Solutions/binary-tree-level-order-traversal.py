"""
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""


def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res