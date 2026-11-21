class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[0,0]
        for i in nums1:
            if i in nums2:
                res[0]+=1
        for i in nums2:
            if i in nums1:
                res[1]+=1
        return res
        