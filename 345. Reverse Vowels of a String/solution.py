class Solution:
    def reverseVowels(self, s: str) -> str:
        l=[]
        for i in s:
            if i in "aeiouAEIOU":
                l.append(i)
        l.reverse()
        res=list(s)
        a=0
        for i in range(len(res)):
            if res[i] in "aeiouAEIOU":
                res[i]=l[a]
                a+=1
        return "".join(res)