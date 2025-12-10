class Solution {
    public int maximumWealth(int[][] accounts) {

        int total = max(accounts);
        return total;
    }
    static int max(int[][] arr) {
        int total = 0;
        for(int row = 0; row<arr.length; row++){
            int t = 0;
            for(int col = 0;col<arr[row].length;col++){
                t += arr[row][col];
            }
            if(t>total){
                total = t;
            }
        }
        return total;
    }
}