import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n=int(num**0.5)
        if(n*n==num):
            return True
        return False
