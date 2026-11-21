class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        while insert_pos < n:
            nums[insert_pos] = 0
            insert_pos += 1