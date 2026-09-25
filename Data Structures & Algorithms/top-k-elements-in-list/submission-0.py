import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0:
            return 0

        ans = []
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1

        minheap = []

        for key, value in freq.items():
            heapq.heappush(minheap, [value, key])

            if len(minheap) > k:
                heapq.heappop(minheap)

        for i in minheap:
            ans.append(i[1])

        return ans 