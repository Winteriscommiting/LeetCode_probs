class Solution:
    def numSpecial(self, mat):
        def col_sum(ind):
            return sum(i[ind] for i in mat)
        s=0
        for i in mat:
            if sum(i)==1:
                ind=i.index(1)
                s+=col_sum(ind)==1
        return s