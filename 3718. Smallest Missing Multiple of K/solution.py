class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n=len(nums)
        for i in range(n):
            if (i+1)*k not in nums:
                return (i+1)*k
            else:
                if (i+2)*k not in nums:
                    return (i+2)*k
                