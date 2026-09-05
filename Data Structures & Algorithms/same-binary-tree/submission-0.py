# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p:
            return False
        elif not q:
            return False
            
        if p.val != q.val:
            return False

        # if p.left != q.left or p.right != q.right:
        #      return False 

        temp_left = self.isSameTree(p.left, q.left)
        temp_right = self.isSameTree(p.right, q.right)

        if temp_left and temp_right:
            return True
        else:
            return False