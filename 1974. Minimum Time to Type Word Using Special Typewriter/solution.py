class Solution:
    def minTimeToType(self, word: str) -> int:
        res=0
        temp='a'
        for i in word:
            temp1=abs(ord(i)-ord(temp))
            res+=min(temp1,26-temp1)
            temp=i
        res+=len(word)
        return res