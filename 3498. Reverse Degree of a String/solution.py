class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            res+=(abs(ord(s[i])-ord('a')-26)*(i+1))
        return res
        