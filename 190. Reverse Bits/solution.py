class Solution:
    def reverseBits(self, n: int) -> int:
        b='{:032b}'.format(n)
        st=str(b)[::-1]
        res=int(st,2)
        return res
