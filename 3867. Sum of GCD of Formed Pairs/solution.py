class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd=[0]*len(nums)
        current_max=nums[0]
        prefixGcd[0]=nums[0]
        for i in range(1, len(nums)):
            if nums[i] > current_max:
                current_max = nums[i]
            prefixGcd[i] = math.gcd(nums[i], current_max)
        prefixGcd.sort()
        res=0
        i=0
        j=len(prefixGcd)-1
        while i<j:
            res+=gcd(prefixGcd[i],prefixGcd[j])
            i+=1
            j-=1
        return res
        