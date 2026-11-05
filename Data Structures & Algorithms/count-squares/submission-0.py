from collections import defaultdict
class CountSquares:
    def __init__(self):
        self.points = defaultdict(int)
    
    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1   

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0

        for (px, py), freq in self.points.items():
            if px != x and py != y and abs(px-x) == abs(py-y):
                p1 = (x, py)
                p2 = (px, y)

                ans += (
                    self.points.get((x, py), 0)*
                    self.points.get((px, y), 0)*
                    freq
                )

        return ans