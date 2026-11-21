class Solution:
    def repeatedCharacter(self, s: str) -> str:
        s1=set()
        for i in s:
            if i not in s1:
                s1.add(i)
            else:
                return i