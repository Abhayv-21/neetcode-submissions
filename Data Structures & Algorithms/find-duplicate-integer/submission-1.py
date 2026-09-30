class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        ptr = 0

        while ptr != slow:
            ptr = nums[ptr]
            slow = nums[slow]

        return ptr