class Solution {
    public boolean searchMatrix(int[][] arr, int target) {
        for (int r = 0; r<arr.length; r++){
            for (int col = 0; col<arr[r].length;col++){
                if(arr[r][col] == target){
                    return true;
                }
            }
        }
        return false;
    }
}