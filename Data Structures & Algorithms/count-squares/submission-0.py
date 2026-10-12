class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            # diagonal
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            
            # corner
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res

