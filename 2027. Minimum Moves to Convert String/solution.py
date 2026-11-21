class Solution:
    def minimumMoves(self, s: str) -> int:
        res,i=0,0
        n=len(s)
        while i<n:
            if s[i]=="X":
                res+=1
                i+=2
            i+=1
        return res