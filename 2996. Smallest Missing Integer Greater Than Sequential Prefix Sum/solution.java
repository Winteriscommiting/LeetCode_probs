class Solution {
    public int missingInteger(int[] nums) {
        int s=nums[0];
        for(int i=1;i<nums.length;i++){
            if(nums[i]==nums[i-1]+1){
                s+=nums[i];
            }else{
                break;
            }
        }
        Set<Integer> s1=new HashSet<>();
        for(int i:nums){
            if(i>=s){
                s1.add(i);
            }
        }
        while(s1.contains(s))   s++;
        return s;        
    }
}