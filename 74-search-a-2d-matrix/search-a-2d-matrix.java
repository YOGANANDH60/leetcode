class Solution {
    public boolean searchMatrix(int[][] mat, int target) {
        int r = 0;
        int c = mat[0].length-1;

        while (r < mat.length && c >= 0) {
            if(mat[r][c] == target){
                return true;
            }
            if(mat[r][c] < target){
                r++;
            }
            else{
                c--;

            }
        }
        return false;
    }
}