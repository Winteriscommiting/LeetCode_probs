class Solution:
    def numSquares(self, n: int) -> int:
        dp = [1e9] * (n+1)
        dp[0] = 0
        for i in range(1, 101):
            sq = i ** 2
            if sq > n:
                break
            for curr in range(sq, n+1):
                dp[curr] = min(dp[curr], dp[curr - sq] + 1)
        return dp[-1]