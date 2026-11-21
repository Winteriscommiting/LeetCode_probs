class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return list(combinations([i for i in range(1,n+1)],k))