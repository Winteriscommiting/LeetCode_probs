class Solution:
    def countMonobit(self, n: int) -> int:
        if n<0:
            return 0
        count=1
        current=1
        while current<=n:
            count+=1
            current=current*2+1
        return count
        