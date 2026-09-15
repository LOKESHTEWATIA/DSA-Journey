class Solution {
public:
    int maxPalindromes(string s, int k) {
        int n = s.size();
        int count = 0;
        int last_end = -1;

        // Check if substring s[l..r] is a palindrome
        auto isPalindrome = [&](int l, int r) {
            while (l < r) {
                if (s[l++] != s[r--]) return false;
            }
            return true;
        };

        for (int i = 0; i <= n - k; ++i) {
            // Check length k
            if (i > last_end && isPalindrome(i, i + k - 1)) {
                count++;
                last_end = i + k - 1;
            }
            // Check length k + 1
            else if (i + k < n && i > last_end && isPalindrome(i, i + k)) {
                count++;
                last_end = i + k;
            }
        }

        return count;
    }
};