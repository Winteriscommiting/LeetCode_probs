class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        target = (sum(aliceSizes) - sum(bobSizes))//2
        d = dict()
        for a in aliceSizes:
            d[a] = 1
        for b in bobSizes:
            if d.get(b + target, 0) == 1:
                return [b+target, b]
        return [-1,-1]