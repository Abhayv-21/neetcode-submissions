class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append((timestamp, value)) 
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""

        best = ""
        left = 0
        right = len(self.dic[key]) - 1

        while left <= right:
            mid = (left+right)//2

            if self.dic[key][mid][0] <= timestamp:
                best = self.dic[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return best