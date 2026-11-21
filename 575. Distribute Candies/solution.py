class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        mid=len(candyType)//2
        s=set(candyType)
        if mid>len(s):
            return len(s)
        return mid