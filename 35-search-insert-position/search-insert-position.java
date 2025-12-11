class Solution {
    public int searchInsert(int[] nums, int target) {

        int s = 0;
        int e = nums.length -1;
        
       int ans = search(nums,s,e,target);
       return ans;
    }
    static int search(int[] arr, int s, int e, int target2) {
         
        if(s>e){
            return s;
        }
        int m = s+(e-s) / 2;

         if (arr[m] == target2 ) {
            return m;
         }
         if (target2 < arr[m] ) {
            return search(arr, s, m-1, target2);
         }

        return search(arr, m+1, e, target2);
    }
}