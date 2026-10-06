# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root, lower, upper):
            if not root:
                return True

            if root.val <= lower or root.val >= upper:
                return False
            
            left_result = dfs(root.left, lower, root.val)
            right_result = dfs(root.right, root.val, upper)

            return left_result and right_result

        lower = float('-inf')
        upper = float('inf')
        return dfs(root, lower, upper)

