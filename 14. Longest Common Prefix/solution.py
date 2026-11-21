class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common=""
        if "" in strs:
            return ""
        if len(strs)==1:
            return strs[0]
        c=1
        while True:
            if c==len(strs[0])+1:
                return common
            char=strs[0][:c]
            for i in strs:
                if(char!=i[:c]):
                    return common
            common=char
            c+=1