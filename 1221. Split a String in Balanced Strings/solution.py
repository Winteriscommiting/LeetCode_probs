class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c,c1=0,0
        for i in s:
            if i=='L':
                c+=1
            if i=='R':
                c-=1
            if c==0:
                c1+=1
        return c1