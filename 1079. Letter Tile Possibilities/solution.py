from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        l=list(tiles)
        c=0
        for i in range(1,len(tiles)+1):
            it=permutations(tiles,i)
            c+=len(set(it))
        return c