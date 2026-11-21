class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums) 

    def reset(self) -> List[int]:
        self.nums = list(self.original)
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled_nums = list(self.nums) 
        random.shuffle(shuffled_nums)
        return shuffled_nums