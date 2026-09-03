class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for i in nums:
            if i not in visited:
                visited.add(i)

        if len(visited) != len(nums):
            return True
        else:
            return False