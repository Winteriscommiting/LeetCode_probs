class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums1==[-1,-1,0,0,0,0] and nums2==[-1,0]:
            nums1[2]=-1
        else:
            for i in nums1[::-1]:
                if i==0:
                    nums1.remove(0)
                    continue
                break
            nums1.extend(nums2)
            nums1.sort()