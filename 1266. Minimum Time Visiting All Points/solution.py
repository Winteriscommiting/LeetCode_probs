class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        p1=0
        for i in range(len(points) - 1):
            a=abs(points[i+1][0]-points[i][0])
            b=abs(points[i+1][1]-points[i][1])
            p1+=max(a,b)
        return p1