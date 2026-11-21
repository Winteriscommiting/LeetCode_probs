class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            s=0
            while n!=0:
                d=n%10
                s+=d*d
                n=n//10
            if s<10:
                if s==1 or s==7:
                    return True
                return False
            n=s