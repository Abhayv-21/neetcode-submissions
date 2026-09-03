class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)-1
        for _ in range(len(nums)):
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1

        return -1