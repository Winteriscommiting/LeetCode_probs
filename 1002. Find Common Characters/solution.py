class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=[]
        temp=set(words[0])
        for i in temp:
            a=min([j.count(i) for j in words])
            res+=[i]*a
        return res