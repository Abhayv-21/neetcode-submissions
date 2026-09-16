class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        memo = {}

        def dfs(index, curr_sum):
            if index == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0
            
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]

            add = dfs(index+1, curr_sum+nums[index])
            sub = dfs(index+1
            , curr_sum-nums[index])

            memo[(index, curr_sum)] = add+sub
            return memo[(index, curr_sum)]
        return dfs(0, 0)