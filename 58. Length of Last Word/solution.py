class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        s=list(s)
        return len(s[len(s)-1])