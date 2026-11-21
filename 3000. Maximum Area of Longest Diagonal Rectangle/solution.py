class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_d_sq = 0
        max_area = 0
        for i in dimensions:
            j, k = i[0], i[1]
            d_sq = j**2 + k**2
            area = j * k
            if d_sq > max_d_sq:
                max_d_sq = d_sq
                max_area = area
            elif d_sq == max_d_sq:
                if area > max_area:
                    max_area = area
        return max_area