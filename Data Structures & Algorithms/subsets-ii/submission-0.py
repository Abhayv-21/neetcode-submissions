class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(index, curr):
            ans.append(curr.copy()) 
            if index==len(nums):
                return

            for i in range(index, len(nums)):
                if i>index and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        index = 0
        curr = []
        backtrack(index, curr)
        return ans