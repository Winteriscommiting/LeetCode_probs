class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        while num>0:
            div=num%10
            s+=div
            num//=10
        if s<10:
            return s
        return self.addDigits(s)