class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums1)):
            n=nums2.index(nums1[i])
            c=0
            for j in range(n,len(nums2)):
                if nums2[j]>nums1[i]:
                    res.append(nums2[j])
                    c=1
                    break
            if not c:
                res.append(-1)
        return res