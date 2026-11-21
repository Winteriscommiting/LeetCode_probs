class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)
        
        i = 0
        len_startswith_substr = 0
        while (i < min(len_s1, len_s2, len_s3)):
            if (s1[i] == s2[i] == s3[i]):
                len_startswith_substr += 1
            else:
                break

            i += 1

        if (len_startswith_substr > 0):
            return len_s1 + len_s2 + len_s3 - 3 * len_startswith_substr
        else:
            return -1