import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        heap = []
        for i in stones:
            heapq.heappush(heap, -i)

        while len(heap) >= 2:
            ele1 = (-1)*heapq.heappop(heap)
            ele2 = (-1)*heapq.heappop(heap)

            if ele1 == ele2:
                continue
            elif ele1>ele2:
                heapq.heappush(heap, -(ele1-ele2))
            else:
                heapq.heappush(heap, -(val2-val1))

        if heap:
            return (-1)*heap[0]
        else:
            return 0