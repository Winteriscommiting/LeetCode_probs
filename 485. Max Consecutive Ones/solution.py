class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=c=0
        for i in nums:
            if i==1:
                c+=1
                res=max(c,res)
            else:
                c=0
        return res