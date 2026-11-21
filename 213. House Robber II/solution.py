class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a,b=0,0
        x,y=0,0
        for i in range(len(nums)):
            if i>0:
                c=max(a,b+nums[i])
                b=a
                a=c
            if i<len(nums)-1 or i==0:
                c=max(x,y+nums[i])
                y=x
                x=c
        return max(a,x)