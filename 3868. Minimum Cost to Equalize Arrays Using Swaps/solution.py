class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        if nums1==nums2:
            return 0
        c1=Counter(nums1)
        c2=Counter(nums2)
        d=c1+c2 
        res=0
        for i in d.keys():
            if d[i]%2!=0:
                return -1
            c = c1[i]             
            if c>d[i]//2:
                rem=c-d[i]//2
                res+=rem              
        return res