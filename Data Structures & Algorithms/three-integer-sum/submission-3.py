class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # By this method, we'll not be able to skip duplicates
        # ans = []
        # for i, num in enumerate(nums):
        #     seen = {}
        #     target = -num
        #     for j in range(i+1, len(nums)):
        #         curr = nums[j]
        #         need = target - curr
        #         if need in seen:
        #             ans.append([num, curr, need])
        #         seen[curr] = j
        # return ans

        ans = []
        n = len(nums)
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            target = nums[i]

            left = i+1
            right = n-1

            while left<right:
                total = target + nums[left] + nums[right]

                if total<0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([target, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
        return ans



















