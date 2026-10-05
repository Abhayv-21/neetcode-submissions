from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        def level_order(root):
            if not root:
                return 
            
            curr = []
            queue = deque()

            queue.append(root)
            while queue:
                level_size = len(queue)

                for i in range(level_size):
                    node = queue.popleft()

                    if i == level_size - 1:
                        curr.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return curr

        return level_order(root)