class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        l=[0]*len(nums)
        res=[]
        for i in nums:
            if l[i]:
                res.append(i)
            else:
                l[i]=1
        return res