class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if sum(digits)==len(digits)*9:
            digits=[0]+digits
        c=-1
        while True:
            if digits[c]==9:
                digits[c]=0
                c-=1
            else:
                digits[c]=digits[c]+1
                break
        return digits