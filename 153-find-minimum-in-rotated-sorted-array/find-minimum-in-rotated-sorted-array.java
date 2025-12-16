class Solution {
    public int findMin(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        if(nums[start]<nums[end]){
            return nums[start];
        }
        int ans = findPivot(nums,start,end);
        return nums[ans+1];
    }
    static int findPivot(int[] arr,int start,int end) {
       
        while (start <= end) {
            int mid = start + (end - start) / 2;
            // 4 cases over here
            if (mid < end && arr[mid] > arr[mid + 1]) {
                return mid;
            }
            if (mid > start && arr[mid] < arr[mid - 1]) {
                return mid-1;
            }
            if (arr[mid] <= arr[start]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return -1;
    }
}