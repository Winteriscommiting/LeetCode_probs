class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res=[]
        for i in words:
            l=i.split(separator)
            for j in l:
                if j:
                    res.append(j)
        return res