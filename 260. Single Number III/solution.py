class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res=[]
        d={}
        for i in nums:
            d[i]=0
        for i in nums:
            d[i]+=1
        for i in nums:
            if d[i]==1:
                res.append(i)
        return res