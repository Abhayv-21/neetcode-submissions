class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(index, current):
            if index == len(nums):
                ans.append(current.copy())
                return

            current.append(nums[index])
            backtrack(index+1, current)
            current.pop()

            backtrack(index+1, current)
        
        index = 0
        current = []
        backtrack(index, current) 
        return ans