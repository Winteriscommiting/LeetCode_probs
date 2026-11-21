class Solution:
    def reverse(self, x: int) -> int:
        lim=2147483648
        if x<0:
            st=str(x)[1:]
            val=-int(st[::-1])
        else:
            st=str(x)
            val=int(st[::-1])
        if val>-lim and val<lim:
            return val
        return 0