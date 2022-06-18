"""
Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""


def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    queue = [root]
    res = []
    check_even = 0
    while queue:
        check_even += 1
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if check_even % 2 == 1:
            res.append(level)
        else:
            res.append(level[::-1])
    return res
