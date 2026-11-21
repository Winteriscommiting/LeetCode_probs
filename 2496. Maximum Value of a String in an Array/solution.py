class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(len(i) if not i.isdigit() else int(i) for i in strs)    