class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        d={}
        s=set(bulbs)
        for i in s:
            d[i]=False
        for i in bulbs:
            if d[i]==False:
                d[i]=True
            elif d[i]==True:
                d[i]=False
        res=[]
        for i,j in d.items():
            if j==True:
                res.append(i)
        res.sort()
        return res