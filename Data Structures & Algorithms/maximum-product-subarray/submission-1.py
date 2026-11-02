class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            prev_max = curr_max
            prev_min = curr_min
            curr_max = max(num, prev_max*num, prev_min*num)
            curr_min = min(num, prev_max*num, prev_min*num)
            result = max(curr_max, curr_min, result)

        return result