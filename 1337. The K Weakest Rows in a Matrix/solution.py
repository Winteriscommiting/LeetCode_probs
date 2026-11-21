class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d={}
        for i in range(len(mat)):
            c=0
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    c+=1
            d[i]=c
        s=sorted(d,key=d.get)
        return s[:k]