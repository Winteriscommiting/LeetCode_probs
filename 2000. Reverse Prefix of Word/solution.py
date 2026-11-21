from collections import deque
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack=deque()
        ind=0
        if ch not in word:
            return word
        for i in range(len(word)):
            stack.append(word[i])
            if word[i]==ch:
                ind=i
                break
        s=""
        for i in range(len(stack)):
            s+=stack.pop()
        s+=word[ind+1::]
        return s