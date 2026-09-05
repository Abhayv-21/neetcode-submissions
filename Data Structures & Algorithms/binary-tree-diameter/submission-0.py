from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        max_daimeter = 0

        def dfs(node):
            nonlocal max_daimeter

            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            curr_daimeter = left_height + right_height
            max_daimeter = max(max_daimeter, curr_daimeter)

            max_height = 1 + max(left_height, right_height)
            return max_height

        dfs(root)
        return max_daimeter