class Solution:
    def distinctAverages(self, nums: List[int]) -> int: 
       nums.sort()  
       arr = [] 
       i = 0 
       j = len(nums)-1
       for n in nums:
        avg = (nums[i] + nums[j]) / 2 
        arr.append(avg)   
        i +=1 
        j -=1
       length = len(set(arr)) 
       return length