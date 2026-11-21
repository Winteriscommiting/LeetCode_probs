class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={'2':["a","b","c"],'3':["d","e","f"],'4':["g","h","i"],'5':["j","k","l"],'6':["m","n","o"],'7':["p","q","r","s"],'8':["t","u","v"],'9':["w","x","y","z"]}
        if len(digits)==1:
            return d[digits]
        current=d[digits[0]]
        for k in digits[1:]:
            temp=[]
            for i in current:
                for j in d[k]:
                    temp.append(i+j)
            current=temp.copy()
            temp.clear()
        return current