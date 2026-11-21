class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"IV":4,"IX":9,"V":5,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"CM":900,"D":500,"M":1000}
        rm=""
        t=0
        for i in s:
            rm+=i
            if rm not in d:
                t+=d[rm[:-1]]
                rm=rm[-1]
        t+=d[rm]
        return t