class Solution:
    def maxFreqSum(self, s: str) -> int:
        d={'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        for i in s:
            d[i]+=1
        vow_max=0
        con_max=0
        for i,j in d.items():
            if i in "aeiou":
                vow_max=max(j,vow_max)
            else:
                con_max=max(j,con_max)
        return vow_max+con_max
