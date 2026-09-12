class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            memo = {}
            
            def dfs(i):
                if i>=len(arr):
                    return 0
                
                if i in memo:
                    return memo[i]
                
                memo[i] = max(arr[i]+dfs(i+2), dfs(i+1))
                return memo[i]
            return dfs(0)

        return max(helper(nums[1:]), helper(nums[:-1]))
