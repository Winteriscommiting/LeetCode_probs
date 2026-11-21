class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini=nums[0]
        maxi=nums[0]
        pre_max=maxi
        pre_min=mini
        res=nums[0]
        for i in range(1,len(nums)):
            maxi=max(nums[i],pre_max*nums[i],pre_min*nums[i])
            mini=min(nums[i],pre_max*nums[i],pre_min*nums[i])
            pre_max=maxi
            pre_min=mini
            res=max(maxi,res)
        return res