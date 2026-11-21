class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s=n*(n+1)//2
        s1=sum(nums)
        s2=sum(set(nums))
        return [s1-s2,s-s2]