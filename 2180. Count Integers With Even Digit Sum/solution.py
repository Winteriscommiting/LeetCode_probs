class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(1,num+1):
            l=[int(j) for j in str(i)]
            print(l)
            if sum(l)%2==0:
                c+=1
        return c