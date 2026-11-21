class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[nums[i%len(nums)] for i in range(2*len(nums))]
        return ans
        