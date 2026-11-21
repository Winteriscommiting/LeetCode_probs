class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        pos = k
        size = 0
        inverse = 0
        
        for i in range(n):
            size = size*2 + 1
        
        while size != 1:
            if pos < size//2 + 1:
                size = size//2
            elif pos == size//2 + 1:
                return str((inverse+1)%2)
            else:
                pos = size - pos + 1
                size = size//2
                inverse += 1

        return str((inverse)%2)