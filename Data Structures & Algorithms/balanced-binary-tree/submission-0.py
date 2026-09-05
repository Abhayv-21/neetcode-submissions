# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # balance = 0
        root_height = 0

        def dfs(node):
            # nonlocal balance
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if left_height == -1 or right_height == -1:
                return -1

            if abs(left_height-right_height) > 1:
                return -1
            node_height = 1+max(left_height, right_height)

            return node_height

        if dfs(root) == -1:
            return False
        else:
            return True