class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        temp=-1
        flag=True
        for i in s.split():
            if i.isdigit():
                if temp>=int(i):
                    return False
                temp=int(i)
        return True
        