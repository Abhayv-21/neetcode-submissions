from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()

        if not root:
            return ans

        queue = deque()
        queue.append(root)

        while queue:
            curr = []
            level_size = len(queue)
            for _ in range(level_size):
                rot = queue.popleft()
                curr.append(rot.val)
                if rot.left:
                    queue.append(rot.left)
                if rot.right:
                    queue.append(rot.right)
            ans.append(curr)
        return ans