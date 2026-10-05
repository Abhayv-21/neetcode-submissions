# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root:
            return False
        elif not subRoot:
            return False

        def same_tree(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1:
                return False
            elif not root2:
                return False   
            else:
                if root1.val != root2.val:
                    return False

                left_tree = same_tree(root1.left, root2.left)
                right_tree = same_tree(root1.right, root2.right)

                return left_tree and right_tree    

        return same_tree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)