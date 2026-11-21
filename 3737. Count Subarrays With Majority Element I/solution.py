class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            t=0
            for j in range(i,n):
                if nums[j]==target:
                    t+=1
                a=j-i+1
                if t>a//2:
                    c+=1
        return c