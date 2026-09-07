class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start, target, curr):
            if target == 0:
                ans.append(curr.copy())
                return 

            for i in range(start, len(nums)): 
                if nums[i] > target:
                    continue
                curr.append(nums[i])
                new_target = target - nums[i]
                backtrack(i, new_target, curr) 
                curr.pop()

        curr = []
        start = 0
        backtrack(start, target, curr)
        return ans