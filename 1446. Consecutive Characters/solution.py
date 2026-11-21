class Solution:
    def maxPower(self, s: str) -> int:
        maxi=1
        cur=1
        for i,j in enumerate(s[1:],1):
            if j==s[i-1]:
                cur+=1
                maxi=max(maxi,cur)
            else:
                cur=1
        return maxi