class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=list(map(lambda x:ord(x),s))
        l=l[::-1]
        for i in range(0,len(s)):
            s[i]=chr(l[i])