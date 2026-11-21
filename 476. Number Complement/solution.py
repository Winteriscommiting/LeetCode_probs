class Solution:
    def findComplement(self, num: int) -> int:
        return int(len(bin(num)[2:])*'1',2) ^ num