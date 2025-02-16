class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for idx in range(len(points)-1):
            p1 = abs(points[idx][0] - points[idx+1][0])
            p2 = abs(points[idx][1] - points[idx+1][1])
            chebyDist = max(p1, p2)
            res+= chebyDist
        return res