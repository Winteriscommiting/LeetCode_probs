class Solution {
    public long maximumTripletValue(int[] nums) {
        long s=0;
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                for(int k=j+1;k<nums.length;k++){
                    s=Math.max(s,(long)(nums[i]-nums[j])*nums[k]);
                }
            }
        }   
        return s;
    }
}