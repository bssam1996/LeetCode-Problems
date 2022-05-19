"""
Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
"""


def preorderTraversal(self, root):
    def returning_value(node, current_list):
        if node is None:
            return
        current_list.append(node.val)
        returning_value(node.left, current_list)
        returning_value(node.right, current_list)

    what_to_return = []
    returning_value(root, what_to_return)
    return what_to_return
