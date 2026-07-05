class Solution {
    public void moveZeroes(int[] nums) {
        int o=0;
        for(int x=0;x<nums.length;x++){
            if(nums[x]!=0){
                nums[o++]=nums[x];
            }
        }
        while(o<nums.length){
            nums[o++]=0;
        }
    }
}
