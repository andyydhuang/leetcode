class Solution {
    public void rotate(int[] nums, int k) {
        int new_k = (k % nums.length);
        //No need to rotate
        if (new_k == 0) {
            return;
        }
        //Rotate point
        int target_idx = nums.length - new_k;

        //Split to two subarrays by rotate point  
        int[] first = Arrays.copyOfRange(nums,target_idx,target_idx+new_k);
        int[] second = Arrays.copyOfRange(nums,0,target_idx);

        //Put right subarray to left and left subarray to right
        System.arraycopy(first, 0, nums, 0, first.length);
        System.arraycopy(second, 0, nums, first.length, second.length);
    }
}