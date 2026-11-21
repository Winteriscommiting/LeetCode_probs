class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0: 
            return "0"
        res=""
        n1=abs(num)
        while n1>0:
            rem=n1%7
            res=str(rem)+res  
            n1//=7
        return "-" + res if num<0 else res       
        