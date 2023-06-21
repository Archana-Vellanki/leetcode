public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        System.out.println(left + " " + right);
        while (left < right) {
            int mid = (int) (left + (right - left) / 2);
            System.out.println(left + " " + right + " " + mid);
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return (left);
    }
}
