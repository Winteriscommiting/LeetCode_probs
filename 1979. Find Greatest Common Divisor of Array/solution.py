class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m1=min(nums)
        m2=max(nums)
        return math.gcd(m1,m2)