import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for i in tasks:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        heap = []
        for task,freq in dic.items():
            heapq.heappush(heap, (-freq, task))

        queue = []
        time = 0
        
        while heap or queue:
            time += 1
            
            while queue and queue[0][2] <= time:
                freq, val, avaiable_time = queue.pop(0)
                heapq.heappush(heap, (freq, val))

            if heap:
                freq, task = heapq.heappop(heap)
                freq += 1

                if freq != 0:
                    available_time = time+n+1
                    queue.append([freq, task, available_time])

        return time