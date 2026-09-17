class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int n = arr.length;
        // dp[i] stores the minimum length of a valid subarray found in arr[0...i-1]
        int[] dp = new int[n + 1];
        int INF = Integer.MAX_VALUE / 2;
        dp[0] = INF;

        int ans = INF;
        int left = 0, currentSum = 0;

        for (int right = 0; right < n; right++) {
            currentSum += arr[right];

            while (currentSum > target) {
                currentSum -= arr[left++];
            }

            dp[right + 1] = dp[right];

            if (currentSum == target) {
                int currentLen = right - left + 1;
                // Combine with the best non-overlapping subarray before index 'left'
                ans = Math.min(ans, currentLen + dp[left]);
                // Update the best single subarray seen so far
                dp[right + 1] = Math.min(dp[right + 1], currentLen);
            }
        }

        return ans >= INF ? -1 : ans;
    }
}