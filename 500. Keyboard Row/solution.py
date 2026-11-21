class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row="qwertyuiop"
        second_row="asdfghjkl"
        third_row="zxcvbnm"
        l=[]
        for i in words:
            a=i.lower()
            if len(set(first_row+a))==len(first_row) or len(set(second_row+a))==len(second_row) or len(set(third_row+a))==len(third_row):
                l.append(i)
        return l