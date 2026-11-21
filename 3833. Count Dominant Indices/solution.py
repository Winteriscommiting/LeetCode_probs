class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        c=0
        while len(nums)>0:
            a=nums.pop(0)
            if len(nums)==0:
                return c
            if a>sum(nums)/len(nums):
                c+=1
        return c 