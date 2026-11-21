class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['']*len(s)
        for i,j in enumerate(s):
            res[indices[i]]=j
        return "".join(res)
