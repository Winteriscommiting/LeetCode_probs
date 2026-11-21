class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd=0
        min_even=float("inf")
        d=Counter(s)
        for i in d.values():
            if i%2!=0:
                max_odd=max(i,max_odd)
            else:
                min_even=min(i,min_even)
        return max_odd-min_even