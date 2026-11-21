class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s1=sum(nums)
        l=[str(i) for i in nums]
        s2=0
        for i in l:
            for j in i:
                s2+=int(j)
        return abs(s1-s2)
