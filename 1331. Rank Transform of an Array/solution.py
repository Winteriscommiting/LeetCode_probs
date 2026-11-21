class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=sorted(set(arr))
        d={}
        for i,j in enumerate(s):
            d[j]=i+1
        res=[]
        for i in arr:
            res.append(d[i])
        return res