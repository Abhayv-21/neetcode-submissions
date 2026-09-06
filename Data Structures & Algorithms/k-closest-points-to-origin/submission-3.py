import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        def dis(arr):
            return (arr[0])**2 + (arr[1])**2

        for i in points:
            if len(heap) < k:
                heapq.heappush(heap, (-dis(i), i))
            else:
                if dis(i) < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-dis(i), i))

        ans = []
        for i in heap:
            ans.append(i[1])
        return ans