class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l={'a':-1,'b':-1,'c':-1}
        c=0
        for i,j in enumerate(s):
            l[j]=i
            if l['a']!=-1 and l['b']!=-1 and l['c']!=-1:
                m=min(l['a'],l['b'],l['c'])
                c+=m+1
        return c