class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int start = 1 ;
        int end  = 0;
        for (int p : piles){ end = Math.max(end,p);}
        while(start < end){
            int mid = start+ (end-start) /2;
            if(cile(piles,h,mid)){
                end = mid;
            }
            else{
                start = mid+1;
            }
        }
        return start;
    }
    static boolean cile(int[] piles,int h,int k){
        int hours = 0;
        for (int p:piles){
            hours +=(p+ k - 1)/k;
        }
        return hours<=h;
    }
}