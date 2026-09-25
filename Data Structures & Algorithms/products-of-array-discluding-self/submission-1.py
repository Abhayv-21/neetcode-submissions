class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n

        left = [1]*(n+1)
        left[0] = 1

        right = [1]*(n+1)
        right[n] = 1

        for i in range(1, n):
            left[i] = left[i-1]*nums[i-1]

        for i in range(n-1, -1, -1):
            right[i] = right[i+1]*nums[i]

        for i in range(n):
            ans[i] = left[i]*right[i+1] 

        return ans