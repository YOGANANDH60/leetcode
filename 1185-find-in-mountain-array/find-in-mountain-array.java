class Solution {

    public int findInMountainArray(int target, MountainArray mountainArr) {

        int peak = peakIndexInMountainArray(mountainArr);

        int first = agsearch(mountainArr, target, 0, peak);
        if (first != -1) {
            return first;
        }

        return agsearch(mountainArr, target, peak + 1, mountainArr.length() - 1);
    }

    // Peak finder
    public int peakIndexInMountainArray(MountainArray arr) {
        int s = 0;
        int e = arr.length() - 1;

        while (s < e) {
            int mid = s + (e - s) / 2;

            if (arr.get(mid) > arr.get(mid + 1)) {
                e = mid;
            } else {
                s = mid + 1;
            }
        }
        return s;
    }

    // Order-agnostic binary search
    static int agsearch(MountainArray arr, int target, int s, int e) {

        boolean asc = arr.get(s) < arr.get(e);

        while (s <= e) {
            int m = s + (e - s) / 2;
            int val = arr.get(m);

            if (val == target) {
                return m;
            }

            if (asc) {
                if (target > val) {
                    s = m + 1;
                } else {
                    e = m - 1;
                }
            } else {
                if (target > val) {
                    e = m - 1;
                } else {
                    s = m + 1;
                }
            }
        }
        return -1;
    }
}
