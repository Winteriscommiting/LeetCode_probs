class Solution {
    public int lengthOfLongestSubstring(String s) {
        boolean[] arr=new boolean[128];
        int c=0;
        int left=0;
        int right=0;
        while(right<s.length()){
            if(!arr[s.charAt(right)]){
                arr[s.charAt(right)]=true;
                c=Math.max(c,right-left+1);
                right++;
            } else {
                arr[s.charAt(left)]=false;
                left++;
            }
        }
        return c;
    }
}