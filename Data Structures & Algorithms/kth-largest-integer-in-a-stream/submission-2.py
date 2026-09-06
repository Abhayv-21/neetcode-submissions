import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.minheap = []
        for i in nums:
            if len(self.minheap) < k:
                heapq.heappush(self.minheap, i)
            else:
                if i > self.minheap[0]:
                    heapq.heappop(self.minheap)
                    heapq.heappush(self.minheap,i)

    def add(self, val: int) -> int:
        if len(self.minheap) == self.k:
            if val > self.minheap[0]:
                heapq.heappop(self.minheap)
                heapq.heappush(self.minheap,val)
                return self.minheap[0]
            else:
                return self.minheap[0]
        else:
            heapq.heappush(self.minheap, val)
            return self.minheap[0]