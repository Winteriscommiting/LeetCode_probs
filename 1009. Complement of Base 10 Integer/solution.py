class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=list(bin(n)[2::])
        for i in range(len(s)):
            if s[i]=='1':
                s[i]='0'
                continue
            s[i]='1'
        res="".join(s)
        return int(res,2)