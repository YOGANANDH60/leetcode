class Solution {
    public int search(int[] arr, int target) {
        int ans = searchh(arr,target);
        return ans;
    }
   static int searchh(int[] arr,int target){
        int s = 0;
        int e = arr.length-1;

        while (s<= e) {
            int mid = s+(e-s) /2;

            if(arr[mid] == target){
                return mid;
            }

            // left side

            if(arr[s]<=arr[mid]){
                if(target>=arr[s] && target < arr[mid]){
                    e = mid-1;
                }
                else
                {
                    s = mid + 1;
                }
            }
            else{
                if(target>arr[mid] && target <= arr[e]){
                    s = mid + 1;

                }
                else
                {
                    e = mid-1;
                }
            }
        }
        return -1;
    }
}