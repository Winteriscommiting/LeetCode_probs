class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k=len(nums)
        sum1=(k*(k+1))//2
        return sum1-sum(nums)