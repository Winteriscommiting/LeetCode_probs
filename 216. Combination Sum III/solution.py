class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        min_sum=sum([i for i in range(k)])
        if n<min_sum:
            return []
        res=[]
        comb=list(combinations([i for i in range(1,10)],k))
        for i in comb:
            if sum(i)==n:
                res.append(i)
        return res