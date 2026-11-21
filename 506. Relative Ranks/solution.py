class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp=sorted(score, reverse=True)
        res=[]
        for i in range(len(score)):
            if score[i]==temp[0]:
                res.append("Gold Medal")
            elif score[i]==temp[1]:
                res.append("Silver Medal") 
            elif score[i]==temp[2]:
                res.append("Bronze Medal")
            else:
                res.append(str(temp.index(score[i])+1))
        return res
