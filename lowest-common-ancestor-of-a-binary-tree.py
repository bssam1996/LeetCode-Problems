"""
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
"""


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    self.values = {}

    def invest_tree(node, parents, p, q):
        if node is None:
            return None
        if node.val == p or node.val == q:
            self.values[node.val] = parents + [node]
        if len(self.values) == 2:
            return None
        invest_tree(node.left, parents + [node], p, q)
        invest_tree(node.right, parents + [node], p, q)

    invest_tree(root, [], p.val, q.val)
    p_parents = self.values[p.val]
    q_parents = self.values[q.val]
    if len(p_parents) > len(q_parents):
        q_parents_set = set(q_parents)
        for element in p_parents[::-1]:
            if element in q_parents_set:
                return element
    else:
        p_parents_set = set(p_parents)
        for element in q_parents[::-1]:
            if element in p_parents_set:
                return element