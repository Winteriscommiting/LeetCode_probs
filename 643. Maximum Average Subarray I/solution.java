class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int res=0;
        for (int i=0;i<k;i++)   res+=nums[i];
        double maxAvg=(double)res/k;
        for (int i=1;i<=nums.length-k;i++) {
            res=res-nums[i-1]+nums[i+k-1];
            maxAvg=Math.max(maxAvg,(double)res/k);
        }
        return maxAvg;
    }
}