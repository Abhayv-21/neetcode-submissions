# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        cnt = 0

        def dfs(root):
            nonlocal cnt
            if not root:
                return 
            maxi = 0
            
            stack = []
            stack.append((root, root.val))

            while stack:
                node, maxi = stack.pop()
                if node.val >= maxi:
                    cnt += 1
                maxi = max(maxi, node.val)
                if node.right:
                    stack.append((node.right, maxi))
                if node.left:
                    stack.append((node.left, maxi)) 

        dfs(root)
        return cnt