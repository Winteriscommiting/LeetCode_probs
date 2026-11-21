class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        print(n)
        if n<=8:
            return n
        elif n>8 and n<=16:
            return 8+(2*(n-8))
        elif n>16 and n<=24:
            return 8+(2*(16-8))+(3*(n-16))
        else:
            if n==25:
                return 9+(2*(16-8))+(3*(n-16))
            else:
                return 10+(2*(16-8))+(3*(n-16))