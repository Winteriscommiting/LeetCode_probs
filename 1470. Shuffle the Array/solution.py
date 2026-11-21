class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        j=0
        num=[0]*(2*n)
        for i in range(n):
            num[j]=nums[i]
            num[j+1]=nums[i+n]
            j+=2
        return num