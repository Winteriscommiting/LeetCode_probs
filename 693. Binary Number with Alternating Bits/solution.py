class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        l=[]
        while n>0:
            r=n%2
            l.append(r)
            n=n//2
        for i in range(len(l)-1):
            if not l[i]^l[i+1]:
                return False
        return True