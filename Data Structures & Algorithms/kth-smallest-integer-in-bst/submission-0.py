# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        cnt = 0
        ans = 0
        
        def inorder(root, k):
            nonlocal cnt, ans
            if not root:
                return 

            inorder(root.left, k)
            cnt += 1
            if cnt == k:
                ans = root.val
                return ans

            inorder(root.right, k) 

        inorder(root, k)
        return ans